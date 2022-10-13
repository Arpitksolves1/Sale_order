# -*- coding: utf-8 -*-


{
    'name': 'Sale Order Line',
    'version': '1.0.0',
    'category': 'Sale Order',
    'sequence': 1,
    'summary': 'Sale Order Line',
    'description': "Add one field in already exist one2many field",
    'depends': ['base', 'sale', 'account'],
    'data': [
        'views/sale_order_view.xml',
        'views/sale_invoice_view.xml'

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
}
