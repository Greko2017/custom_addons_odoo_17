from odoo import api, fields, models

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    
    name = fields.Char('Name', required=True )
    active = fields.Boolean('Active', default=True )
    color = fields.Integer('Color' )
    color_2 = fields.Char('Color 2' )
