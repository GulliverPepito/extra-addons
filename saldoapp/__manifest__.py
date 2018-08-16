# -*- coding: utf-8 -*-
{
    'name': "Saldo App",

    'summary': """
        Controla tus ingresos y egresos con Saldo App - Summary""",

    'description': """
        Description
    """,

    'author': "popehiflo - Pool Hijuela",
    'website': "https://github.com/popehiflo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}