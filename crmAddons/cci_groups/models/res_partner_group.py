from odoo import fields, models


class CciPartnerGroup(models.Model):
    _name = 'res.partner.group'
    name = fields.Char('Group Name')
    code = fields.Char('Abbreviation')
    partner_ids = fields.Many2many('res.partner')
