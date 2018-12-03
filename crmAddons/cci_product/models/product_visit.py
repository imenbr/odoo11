from odoo import fields, models


class CciProductVisit(models.Model):
    _name = 'cci_product.product_visit'
    name = fields.Many2one('res.partner', string='Visitors')
    visitors_product_ids = fields.Many2one('product.template', string='Product')
    visit_date = fields.Date(string='Visit Date')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    note = fields.Char(string="Note")
