# -*- coding: utf-8 -*-
{
    'name': "hearthstodoo",

    'summary': """Listado de cartas""",
    
    'description': """
        modulo basico con un listado sencillo de cartas de hearthstone
    """,

    'icon': "/modulo/static/img/icon.png",
    'author': "Sergio vicente",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Listados',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
