# Copyright 2024 Stéphan Sainléger ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "lok_rocketchat_notifications",
    "version": "14.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Stéphan Sainléger",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Define the content of notifications sent to Rocketchat",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "mail_message_rocketchat",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        # "security/security.xml",
        # "security/ir.model.access.csv",
        # "views/menu.xml",
        # "data/data.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}