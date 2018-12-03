from odoo import fields, models


class CciProductAttendee(models.Model):
    _name = 'cci_product.product_session'
    name = fields.Char(string='Title')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    sessions_products_ids = fields.Many2one('product.template', string='Product')
