{
    'name' : 'Product Rules',
     'version': '19.0.1.0.0',
    'author' : 'Digital',
    'category' :'Product',
    'license' : 'LGPL-3',
    'depends' : ['stock','auto_fill'],
    'summary' : 'Set rules to product',
    'data' : [
        'security/ir.model.access.csv',
        'views/product_inherit_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'productrules/static/src/js/product_code_display.js',
        ],
    },
    'installable' :True,
    'application' :True,
}
