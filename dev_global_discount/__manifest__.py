# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd. (<http://devintellecs.com>).
#
##############################################################################
{
    "name": "Sale,Purchase & Invoice Discount with Accounting Entries",
    "category": 'Sale',
    "summary": """
                  Apps will set global Fixed/Percentage discount in Sale, Purchase, Invoice with accounting Entries.
        """,
    "description": """
        Apps will set global Fixed/Percentage discount in Sale, Purchase, Invoice with accounting Entries.
    """,
    "sequence": 1,
    "author": "DevIntelle Consulting Service Pvt.Ltd",
    "website": "http://www.devintellecs.com",
    "version": '1.0',
    "depends": ['sale','account','purchase'],
    "images": ['images/main_screenshot.jpg'],
    "data": [
        'views/sale_order_view.xml',
        'views/account_account_view.xml',
        'views/account_invoice_view.xml',
        'views/purchase_order_view.xml',
        'views/discount_field_sale_report.xml',
        'views/discount_field_purchase_report.xml',
        'views/discount_field_invoice_report.xml',
        
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    'price':45.0,
    'currency':'EUR',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
