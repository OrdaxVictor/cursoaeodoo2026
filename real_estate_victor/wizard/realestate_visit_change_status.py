from odoo import fields, models


class RealEstateVisitChangeStatus(models.TransientModel):
    _name = "realestate.visit.change.status"
    _description = "Wizard to change the status of visits"

    status = fields.Many2one(
        comodel_name="realestate.visit.status",
        string="Status",
        required=True
    )

    def action_change_status(self):
        visits = self.env["realestate.visit"].browse(
            self.env.context.get("active_ids", [])
        )
        visits.write({"status": self.status})
        return {
            "type": "ir.actions.act_window",
            "name": "Visits",
            "res_model": "realestate.visit",
            "view_mode": "list",
            "domain": [("id", "in", visits.ids)],
            "target": "current",
        }