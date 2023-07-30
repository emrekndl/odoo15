# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalMedicalSections(models.Model):
    _name = "hospital.medical_sections"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Medical Sections"
    _rec_name = 'reference'

    doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Doctor', tracking=True)
    
    section_materials_ids = fields.One2many('medical_sections.sections_materials', 'medical_section_id', string='Section Materials')
    
    hide_sales_price = fields.Boolean(string='Hide Sales Prices')
    
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", related='doctor_id.gender')
    
    reference = fields.Char(string='Reference', help='Referece of the patient')
    
    time = fields.Datetime(string='Datetime', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Time', default=fields.Date.context_today)
    
    prescript = fields.Html(string='Prescription')
    
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled')], string='Status', default='draft', required=True)
    
    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        self.reference = self.doctor_id.reference
        print("hello mfasdfasdfasdfasdfasdfasdfsa")
        
    def object_test(self):
        print("Button clicked!!!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': ' Button Clicked Successfull',
                'type': 'rainbow_man',
            }
        }
    
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
    
    def action_done(self):
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
            
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
            
            
            
class SectionsMaterials(models.Model):
    _name = 'medical_sections.sections_materials'
    _description = 'Medical Sections Materials'
    
    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(string='Price', related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    
    medical_section_id = fields.Many2one('hospital.medical_sections', string='Medical Section')