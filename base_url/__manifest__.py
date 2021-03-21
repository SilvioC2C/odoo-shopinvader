# -*- coding: utf-8 -*-
#    Rewrite url Base module for OpenERP
#    Copyright (C) 2013 Akretion (http://www.akretion.com)
#    @author EBII MonsieurB <monsieurb@saaslys.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Base Url",
    "version": "10.0.0.2.0",
    "category": "tools",
    "license": "AGPL-3",
    "summary": "keep history of url for products & categories  ",
    "author": "Akretion, ACSONE SA/NV",
    "website": "https://github.com/shopinvader/odoo-shopinvader",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    "external_dependencies": {"python": ["slugify"]},
    "data": ["views/url_view.xml", "security/ir.model.access.csv"],
    "demo": [],
    "url": "",
    "installable": True,
}
