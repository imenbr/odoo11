from odoo import fields, models


class CciProductAttendeeContact(models.Model):
    _name = 'cci_product.product_attendee_contact'
    name = fields.Many2one('res.partner', string='Contact')
    contact_attendees_ids = fields.Many2one('cci_product.product_attendee', string='Attendees')
    presence = fields.Boolean(string='Presence')
    contact_attendees_products_ids = fields.Many2one('product.template', string='Product')
