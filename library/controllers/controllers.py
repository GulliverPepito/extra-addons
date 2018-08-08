# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/library(http.Controller):
#     @http.route('/extra-addons/library/extra-addons/library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/library/extra-addons/library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/library.listing', {
#             'root': '/extra-addons/library/extra-addons/library',
#             'objects': http.request.env['extra-addons/library.extra-addons/library'].search([]),
#         })

#     @http.route('/extra-addons/library/extra-addons/library/objects/<model("extra-addons/library.extra-addons/library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/library.object', {
#             'object': obj
#         })