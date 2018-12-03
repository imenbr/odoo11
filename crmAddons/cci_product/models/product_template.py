from odoo import fields, models, api


class CciProductProductTemplate(models.Model):
    _inherit = 'product.template'
    stage_ids = fields.Many2one('cci_product.product_stage', string='Product Stages', track_visibility='always',
                                index=True, default=0)
    type = fields.Selection(
        [
            ('Fair_Event', 'Fair and event'),
            ('Training', 'Training'),
            ('visit', 'Visit'),
            ('mem_ship', 'membership')
        ], default='Fair_Event')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    product_ids = fields.One2many('cci_product.product_attendee', inverse_name='attendees_products_ids',
                                  string='Attendees')
    visitor_ids = fields.One2many('cci_product.product_visit', inverse_name='visitors_product_ids',
                                  string='Visitors')
    session_ids = fields.One2many('cci_product.product_session', inverse_name='sessions_products_ids',
                                  string='Sessions')

    contact_ids = fields.One2many('cci_product.product_attendee_contact', inverse_name='contact_attendees_products_ids',
                                  string='Contacts')
