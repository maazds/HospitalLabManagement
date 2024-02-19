# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalLab(http.Controller):
#     @http.route('/hospital_lab/hospital_lab', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_lab/hospital_lab/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_lab.listing', {
#             'root': '/hospital_lab/hospital_lab',
#             'objects': http.request.env['hospital_lab.hospital_lab'].search([]),
#         })

#     @http.route('/hospital_lab/hospital_lab/objects/<model("hospital_lab.hospital_lab"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_lab.object', {
#             'object': obj
#         })
