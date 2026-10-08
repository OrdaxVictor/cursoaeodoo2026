from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        result = super().action_confirm()
        for order in self:
            if order.contract_id:
                continue
            rental_line = order.order_line.filtered(
                lambda line: line.product_id.rental_ok
            )[:1]
            if not rental_line:
                continue
            order.contract_id = self.env["realestate.contract"].create({
                "type": "R",
                "status": "D",
                "partner_id": order.partner_id.id,
                "product_id": rental_line.product_id.id,
                "rent": rental_line.price_subtotal,
            })
        return result
