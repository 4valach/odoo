# -*- coding: utf-8 -*-
{
    'name': "Pokemon",

    'summary': """Pokemon""",
    
    'description': """Sistema de Gestion de Pokemon""",

    'icon': "/pokemon/static/img/pokeball.jpg",
    'author': "VictorS y SergioV",
    'website': "http://www.pokemon.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'RUBRICA_28',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
