# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Library Management Module for Odoo 11
        """,

    'description': """
        Library Management Module for Odoo 11
        
    """,

    'author': "popehiflo - Pool Hijuela",
    'website': "https://github.com/popehiflo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/book_view.xml',
        #'views/templates.xml',
    ],
    'application': True,
}