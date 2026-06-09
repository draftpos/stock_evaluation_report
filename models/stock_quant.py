from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    total_selling_value = fields.Monetary(
        string='Total Value On Selling Price',
        compute='_compute_total_selling_value',
        currency_field='currency_id',
        store=False,
    )

    @api.depends('quantity', 'product_id.lst_price')
    def _compute_total_selling_value(self):
        for quant in self:
            quant.total_selling_value = quant.quantity * quant.product_id.lst_price
