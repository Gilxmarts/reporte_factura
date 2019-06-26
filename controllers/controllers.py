# -*- coding: utf-8 -*-
from odoo import http

# class DesignReport(http.Controller):
#     @http.route('/design_report/design_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/design_report/design_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('design_report.listing', {
#             'root': '/design_report/design_report',
#             'objects': http.request.env['design_report.design_report'].search([]),
#         })

#     @http.route('/design_report/design_report/objects/<model("design_report.design_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('design_report.object', {
#             'object': obj
#         })