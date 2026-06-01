{
    'name': 'Customer Rules',
    'version': '19.0.1.0.0',
    'author': 'Digital',
    'category': 'Customer',
    'license': 'LGPL-3',
    'depends': ['base',],
    'summary': 'Set rules to customer',
    'data': [
        'security/ir.model.access.csv',
        'views/customerrule.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'customerrules/static/src/js/customer_code_display.js',
        ],
    },
    'installable': True,
    'application': True,
}
