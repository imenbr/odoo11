# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CciCrmLead(models.Model):
    _inherit = 'crm.lead'
    product_id = fields.Many2one('product.template', string="Product")

    @api.onchange('product_id')
    def onchange_name(self):
        self.name = self.product_id.name


