# -*- coding: utf-8 -*-
from odoo import http

# class CciPartner(http.Controller):
#     @http.route('/cci_partner/cci_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cci_partner/cci_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cci_partner.listing', {
#             'root': '/cci_partner/cci_partner',
#             'objects': http.request.env['cci_partner.cci_partner'].search([]),
#         })

#     @http.route('/cci_partner/cci_partner/objects/<model("cci_partner.cci_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cci_partner.object', {
#             'object': obj
#         })