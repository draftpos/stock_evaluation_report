from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    total_selling_value = fields.Monetary(
        string='Total Value On Selling Price',
        compute='_compute_total_selling_value',
        currency_field='currency_id',
        store=False,
    )

    @api.depends('qty_available', 'lst_price')
    def _compute_total_selling_value(self):
        for product in self:
            product.total_selling_value = product.qty_available * product.lst_price
