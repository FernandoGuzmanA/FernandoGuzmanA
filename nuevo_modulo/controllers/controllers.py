# -*- coding: utf-8 -*-
# from odoo import http


# class ExtraAddons/nuevoModulo(http.Controller):
#     @http.route('/extra_addons/nuevo_modulo/extra_addons/nuevo_modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra_addons/nuevo_modulo/extra_addons/nuevo_modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra_addons/nuevo_modulo.listing', {
#             'root': '/extra_addons/nuevo_modulo/extra_addons/nuevo_modulo',
#             'objects': http.request.env['extra_addons/nuevo_modulo.extra_addons/nuevo_modulo'].search([]),
#         })

#     @http.route('/extra_addons/nuevo_modulo/extra_addons/nuevo_modulo/objects/<model("extra_addons/nuevo_modulo.extra_addons/nuevo_modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra_addons/nuevo_modulo.object', {
#             'object': obj
#         })
