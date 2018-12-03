# -*- coding: utf-8 -*-
from odoo import http

# class CciProduct(http.Controller):
#     @http.route('/cci_product/cci_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cci_product/cci_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cci_product.listing', {
#             'root': '/cci_product/cci_product',
#             'objects': http.request.env['cci_product.cci_product'].search([]),
#         })

#     @http.route('/cci_product/cci_product/objects/<model("cci_product.cci_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cci_product.object', {
#             'object': obj
#         })