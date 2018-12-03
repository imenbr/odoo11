# -*- coding: utf-8 -*-
from odoo import http

# class CciGroups(http.Controller):
#     @http.route('/cci_groups/cci_groups/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cci_groups/cci_groups/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cci_groups.listing', {
#             'root': '/cci_groups/cci_groups',
#             'objects': http.request.env['cci_groups.cci_groups'].search([]),
#         })

#     @http.route('/cci_groups/cci_groups/objects/<model("cci_groups.cci_groups"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cci_groups.object', {
#             'object': obj
#         })