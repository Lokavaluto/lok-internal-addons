import re
from markdownify import markdownify as md

from odoo import models


class MailChannel(models.Model):
    _inherit = "mail.channel"

    def _remove_html_tags(self, text):
        if not text:
            return "Waiting for description."
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def _build_message_to_post(self, notification, notification_model, notification_record):
        """Build the content of the message sent in Rocketchat channel.
        Te be inherited to modify the message content
        """
        message_to_post = super(MailChannel, self)._build_message_to_post(notification, notification_model, notification_record)
        
        notif_body = notification[1].get("body", False)
        author_id = notification[1].get("author_id", False)
        tracking_fields = notification[1].get("tracking_value_ids")
        subtype_id = notification[1].get("subtype_id")
        if notif_body:
            message_to_post = "[%s] -> %s" % (
                author_id[1] if author_id else "",
                md(
                    notif_body,
                    convert=["b", "i", "p", "a"],
                    heading_style="ATX",
                ),
            )
        elif tracking_fields:
            message_to_post = "☑ [%s] **%s**:\n" % (
                notification_model,
                notification_record.name,
            )
            for field in tracking_fields:
                message_to_post += "%s : %s -> %s\n" % (
                    field.get("changed_field", ""),
                    field.get("old_value", ""),
                    field.get("new_value", ""),
                )
        elif subtype_id:
            message_to_post = "☑ [%s] **%s**\n _by %s_\n %s" % (
                subtype_id[1],
                notification_record.name,
                notification_record.user_id.name,
                self._remove_html_tags(notification_record.description),
            )

        if message_to_post:
            message_to_post += "\n\n **📫 From [lokavaluto.fr](%s/mail/view?model=%s&res_id=%s)** _(click to access)_" % (
                self.env["ir.config_parameter"].sudo().get_param("web.base.url"),
                notification[1].get("model"),
                notification[1].get("res_id"),
            )
        return message_to_post