from odoo import models, api

USAGES = ["inventory"]


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    @api.depends("picking_id.partner_id", "product_id")
    def _compute_analytic_distribution(self):
        for line in self:
            if line.picking_id.location_dest_id.usage in USAGES:
                analytic_account = (
                    line.product_id.product_tmpl_id.expense_analytic_account_id
                )

                if analytic_account:
                    line.analytic_distribution = None
                    distribution = {analytic_account.id: 100}
                    line.analytic_distribution = (
                        distribution or line.analytic_distribution
                    )
                else:
                    distribution = line.env[
                        "account.analytic.distribution.model"
                    ]._get_distribution(
                        {
                            "product_id": line.product_id.id,
                            "product_categ_id": line.product_id.categ_id.id,
                            "partner_id": line.picking_id.partner_id.id,
                            "partner_category_id": line.picking_id.partner_id.category_id.ids,
                            "company_id": line.company_id.id,
                        }
                    )
                    line.analytic_distribution = (
                        distribution or line.analytic_distribution
                    )
