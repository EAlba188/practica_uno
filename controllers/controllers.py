# -*- coding: utf-8 -*-
# from odoo import http


# class PracticaUno(http.Controller):
#     @http.route('/practica_uno/practica_uno/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practica_uno/practica_uno/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practica_uno.listing', {
#             'root': '/practica_uno/practica_uno',
#             'objects': http.request.env['practica_uno.practica_uno'].search([]),
#         })

#     @http.route('/practica_uno/practica_uno/objects/<model("practica_uno.practica_uno"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practica_uno.object', {
#             'object': obj
#         })
