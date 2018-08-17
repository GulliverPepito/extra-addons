# -*- coding: utf-8 -*-
from odoo import http

class Saldoapp(http.Controller):

    @http.route('/saldoapp/saldoapp/', auth='public')
    def index(self, **kw):
        return "<h1>Hello, world</h1>"

#     @http.route('/extra-addons/saldoapp/extra-addons/saldoapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/saldoapp.listing', {
#             'root': '/extra-addons/saldoapp/extra-addons/saldoapp',
#             'objects': http.request.env['extra-addons/saldoapp.extra-addons/saldoapp'].search([]),
#         })

#     @http.route('/extra-addons/saldoapp/extra-addons/saldoapp/objects/<model("extra-addons/saldoapp.extra-addons/saldoapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/saldoapp.object', {
#             'object': obj
#         })