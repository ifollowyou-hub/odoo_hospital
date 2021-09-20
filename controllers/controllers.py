# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class KmHospital(http.Controller):

    @http.route('/patient_webform', type='http', auth='public', website=True)
    def patient_webform(self, **kw):
        return http.request.render('km_hospital.create_patient', {})

    @http.route('/create/webpatient', type="http", auth="public", website=True)
    def create_webpatient(self, **kw):
        # print("\nData Received.....", kw)
        request.env['kmhospital.patient'].sudo().create(kw)
        return request.render("km_hospital.patient_thanks", {})

    # route for show all the patient information
    @http.route('/patient_view', type='http', auth='public', website=True)
    def view_patient_web(self, **kw):
        patients = request.env['kmhospital.patient'].sudo().search([])
        # print("\nData Received.....", patients)
        return http.request.render('km_hospital.view_patient', {
            'patients': patients
        })