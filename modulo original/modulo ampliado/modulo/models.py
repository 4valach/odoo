# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Clase(models.Model):
    _name = 'modulo.clase'
    name = fields.Char(string="Nombre Clase", required=True)
    carta_id = fields.One2many('modulo.carta','clase_id', string="carta")

class Carta(models.Model):
    _name ='modulo.carta'
    name = fields.Char(string="Nombre de carta", required=True)
    coste = fields.Integer(string="coste de mana",required=True)
    ataque = fields.Integer(string="ataque",required=True)
    resistencia = fields.Integer(string="resistencia",required=True)
    puntuacion = fields.Char(string="puntuacion", compute='_calc_punt_carta')
    clase_id = fields.Many2one('modulo.clase', string="clase")



    @api.one
    def _calc_punt_carta(self):
        if (self.coste, self.ataque and self.resistencia):
            	if(self.ataque + self.resistencia >= self.coste*2):
            		self.puntuacion = "buena"	  
            	else:
            		self.puntuacion = "mala"   


    @api.depends('ataque', 'resistencia', 'coste')
    def _puntuacionCarta(self):	
        for a in self:
            if (a.coste, a.ataque and a.resistencia):
            	if(r.ataque + r.resistencia >= r.coste*2):
	            	r.puntuacion = "buena"	  
            	else:
    	        	r.puntuacion = "mala"   
                continue

class CartaAmpliada(models.Model):
	_inherit = 'modulo.carta'
	_name = 'modulo.mazo'
	name = fields.Char(string='Nombre de mazo', required=True)
	rareza = fields.Selection([
		('comun', "comun"),
		('rara', "rara"),
		('epica', "epica"),
		('legendaria', "legendaria"),
		])
	
