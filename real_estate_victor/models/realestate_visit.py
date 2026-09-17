# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RealEstateVisit(models.Model):
    _name = 'realestate.visit'
    _description = 'RealEstateVisit'

    name = fields.Char(string='Visita')
    date = fields.Datetime(string='Fchae')
    property = fields.Many2one(comodel_name='realestate.property')
    contact = fields.Many2one(comodel_name='res.partner', string='Contacto')
    status = fields.Selection([('P', 'Pendiente'), ('V', 'Visitado')],string='Estado')
