from odoo import models, fields


class CciProductProductStage(models.Model):
    _name = "cci_product.product_stage"
    name = fields.Char('Stage Name', required=True)
