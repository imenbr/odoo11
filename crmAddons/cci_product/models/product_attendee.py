from odoo import fields, models


class CciProductAttendee(models.Model):
    _name = 'cci_product.product_attendee'
    name = fields.Many2one('res.partner', string='Attendee')
    attendees_products_ids = fields.Many2one('product.template', string='Product')
