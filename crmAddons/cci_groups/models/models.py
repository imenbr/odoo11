# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class cci_groups(models.Model):
#     _name = 'cci_groups.cci_groups'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100