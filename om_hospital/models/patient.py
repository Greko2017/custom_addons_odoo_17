from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    _description = "Hospital Patient"

    name = fields.Char(
        string='Name', tracking=True
    )
            
    gender = fields.Selection(
        string='Gender', 
        selection=[('male', 'Male'), ('female', 'Female')], tracking=True, default="male"
    )
        
    ref = fields.Char(
        string='Reference',
    )    
    
    active = fields.Boolean(
        string='Active', default=True
    )
    
    # computed field
    
    date_of_birth = fields.Date(
        string='Date Of Birth',
        default=fields.Date.context_today,
    )
            
    age = fields.Integer(
        string='Age', tracking=True, compute='_compute_age'
    )
    
        
    image = fields.Image(
        string='Image'
    )

    
    appointment_id = fields.Many2one(
        string='Appointments',
        comodel_name='hospital.appointment'
    )

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                record.age = today.year - record.date_of_birth.year # ((today.month, today.day) < (record.date_of_birth.month, record.date_of_birth.day))
            else:
                record.age = 0

    
    