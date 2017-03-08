# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Entrenador(models.Model): #Un entrenador tiene varios pokemon
    _name = 'pokemon.entrenador'
    name = fields.Char(string="Nombre del entrenador", required=True)
    entrenador_id = fields.One2many('pokemon.pokemon','pokemon_id', string="Pokemon")

class Pokemon(models.Model): #Varios pokemon tienen un mismo entrenador
    _name = 'pokemon.pokemon'
    name = fields.Char(string="Nombre del pokemon", required=True)
    pokemon_id = fields.Many2one('pokemon.entrenador', string="Entrenador")
    tipo = fields.Many2many('res.parent', 'tipo', 'pokemon_id', 'tipo_id', 'Tipo')
    lvl = fields.Integer(string="Nivel", required=True)
    """longitud = fields.Char(string="Longitud del cabello", compute="_calLongitud")"""

    """@api.one
    def _calLongitud(self):
        if (self.tipo == 'Corto' or self.tipo =='corto' or self.tipo =='Largo' or self.tipo == 'largo'):
            if(self.longitud < 5)
                self.tipo = 'Corto'
            else
                self.tipo = 'Largo'"""

class Tipo(models.Model):
    _inherit = 'pokemon.pokemon'
    pokemon = fields.Many2many('pokemon.pokemon', 'tipo', 'tipo_id', 'pokemon_id', 'pokemon' )