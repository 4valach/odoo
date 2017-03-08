# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Clase(models.Model):
    _name = 'modulo.clase'
    name = fields.Char(string="Nombre Clase", required=True)
    carta_id = fields.One2many('modulo.carta','clase_id', string="carta")


class Carta(models.Model):
    _name ='modulo.carta'
    name = fields.Char(string="Nombre de carta", required=True)
    clase_id = fields.Many2one('modulo.clase', string="clase")
