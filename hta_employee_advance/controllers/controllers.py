# -*- coding: utf-8 -*-
# from odoo import http


# class HtaEmployeeAdvance(http.Controller):
#     @http.route('/hta_employee_advance/hta_employee_advance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_employee_advance/hta_employee_advance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_employee_advance.listing', {
#             'root': '/hta_employee_advance/hta_employee_advance',
#             'objects': http.request.env['hta_employee_advance.hta_employee_advance'].search([]),
#         })

#     @http.route('/hta_employee_advance/hta_employee_advance/objects/<model("hta_employee_advance.hta_employee_advance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_employee_advance.object', {
#             'object': obj
#         })
