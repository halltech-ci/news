# -*- coding: utf-8 -*-
# from odoo import http


# class Rapport1(http.Controller):
#     @http.route('/rapport1/rapport1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rapport1/rapport1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rapport1.listing', {
#             'root': '/rapport1/rapport1',
#             'objects': http.request.env['rapport1.rapport1'].search([]),
#         })

#     @http.route('/rapport1/rapport1/objects/<model("rapport1.rapport1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rapport1.object', {
#             'object': obj
#         })
