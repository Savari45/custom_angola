# -*- coding: utf-8 -*-
{
    'name': ' Product Duplication Check, Auto Suggest Available Products',
    'version': '19.0.1.0.0',
    'summary': 'Auto suggest existing products to avoid duplicates',
    'description': """
        This module helps prevent duplicate product creation
        by auto-suggesting existing products while entering
        product names.

        Features:
        - Auto-suggest existing product names
        - Reduce duplicate product creation
        - Custom auto-fill widget
        - Improves product master data consistency
    """,
    'category': 'Tools',
    'author': 'savari',
    'website': 'https://odoo.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'stock',
        'product',
    ],
    'data': [
        # 'views/product_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/auto_fill/static/src/css/auto_fill.css',
            '/auto_fill/static/src/js/auto_fill.js',
            '/auto_fill/static/src/xml/auto_fill.xml',
        ],
    },
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [
        'static/description/banner.gif',
    ],
}