# -*- coding: utf-8 -*-
from odoo import http

# class CciMail(http.Controller):
#     @http.route('/cci_mail/cci_mail/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cci_mail/cci_mail/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cci_mail.listing', {
#             'root': '/cci_mail/cci_mail',
#             'objects': http.request.env['cci_mail.cci_mail'].search([]),
#         })

#     @http.route('/cci_mail/cci_mail/objects/<model("cci_mail.cci_mail"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cci_mail.object', {
#             'object': obj
#         })