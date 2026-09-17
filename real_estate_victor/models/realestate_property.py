# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RealEstateProperty(models.Model):
    _name = 'realestate.property'
    _description = 'RealEstateProperty'

    name = fields.Char(string='Propiedad')
    desc = fields.Char(string='Descripción')
    size = fields.Float(string='Metros cuadrados')
    user_id = fields.Many2one(comodel_name="res.users", string="Responsable")
