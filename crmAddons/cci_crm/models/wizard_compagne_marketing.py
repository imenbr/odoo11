# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CciCrmWizardCompagneMarketing(models.Model):
    produit = fields.Many2one('product.template', string='Produit')
    groupes = fields.Many2many('res.partner.group', string='Groupes')
    members = fields.Many2many('res.users', string='Membres')
