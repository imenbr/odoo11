# -*- coding: utf-8 -*-
from odoo import http

# class CciCrm(http.Controller):
#     @http.route('/cci_crm/cci_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cci_crm/cci_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cci_crm.listing', {
#             'root': '/cci_crm/cci_crm',
#             'objects': http.request.env['cci_crm.cci_crm'].search([]),
#         })

#     @http.route('/cci_crm/cci_crm/objects/<model("cci_crm.cci_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cci_crm.object', {
#             'object': obj
#         })