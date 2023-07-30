from random import randint
from odoo import api, fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    _rec_name = 'p_name'
    
    def _get_default_color(self):
        return randint(1, 11)
    
    p_name = fields.Char(string='Name', required=True)
    p_active = fields.Boolean(string='Active', default=True)
    p_color = fields.Integer(string='Color', default=_get_default_color)
    p_color2 = fields.Char(string='Color Picker')

class DoctorTag(models.Model):
    _name = 'doctor.tag'
    _description = 'Doctor Tag'
    
    def _get_default_color(self):
        return randint(1, 11)
    
    d_name = fields.Char(string='Name', required=True)
    d_active = fields.Boolean(string='Active', default=True)
    d_color = fields.Integer(string='Color', default=_get_default_color)
    d_color2 = fields.Char(string='Color Picker')
