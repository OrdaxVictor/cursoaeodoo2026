from odoo import models, fields

class RealestatePropertyIncidence(models.Model):
    _name = "realestate.property.incedence"
    _description = "Property Incidence"

    def _default_name(self):
        return "Incidencia "

    name = fields.Char(string="Name", default=_default_name())
    sequence = fields.Integer(string="Sequence", default=10)
    property_id = fields.Many2one(
        comodel_name="realestate.property",
        string="Property",
        ondelete="cascade",
    )
    desc = fields.Text(string="Description")
    priority = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4')], string='Priority')
    status = fields.Selection([('P', 'Pending'),('S','Solved')], string='Status', default='P')
    date = fields.Datetime(string='Date')
    user_id = fields.Many2one(comodel_name='res.users', string='Manager')