# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RealEstateProperty(models.Model):
    _name = 'realestate.property'
    _description = 'RealEstateProperty'

    name = fields.Char(string='Property')
    desc = fields.Char(string='Description')
    size = fields.Float(string='Size')
    user_id = fields.Many2one(comodel_name="res.users", string="Manager")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")
    category_id = fields.Many2one(comodel_name="realestate.category", string="Category")

    price = fields.Float(string="Price")
    reference = fields.Char(string="Reference")
    availability = fields.Boolean(string="Availability", default=True)

    stage_id = fields.Many2one(
        comodel_name="realestate.property.stage",
        string="Stage",
        group_expand="_read_group_stage_ids"
    )

    color = fields.Integer(string="Color")

    def action_reserve(self):
        self.availability = False
    
    def _read_group_stage_ids(self, stages, domain):
        return self.env['realestate.property.stage'].search([], order='sequence')