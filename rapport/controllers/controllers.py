# -*- coding: utf-8 -*-
# from odoo import http


# class Rapport(http.Controller):
#     @http.route('/rapport/rapport/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rapport/rapport/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rapport.listing', {
#             'root': '/rapport/rapport',
#             'objects': http.request.env['rapport.rapport'].search([]),
#         })

#     @http.route('/rapport/rapport/objects/<model("rapport.rapport"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rapport.object', {
#             'object': obj
#         })
