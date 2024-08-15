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

    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='patient.tag',
    )
    
    @api.model
    def create(self, vals):
        # print("Odoo Inherited Patient create", vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.ref')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        # print("Odoo Inherited Patient write", vals)
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.ref')
            
        return super(HospitalPatient, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                record.age = today.year - record.date_of_birth.year # ((today.month, today.day) < (record.date_of_birth.month, record.date_of_birth.day))
            else:
                record.age = 1

                
    # @api.model
    # def name_get(self, ids):
    #     records = self.search(ids)
    #     result = []
    #     for record in records:
    #         name = record.name + ' (' + record.code + ')'
    #         result.append((record.id, name))
    #     return result
    
    
    # def name_get(self):
    #    patient_list = []
    #    for patient in self:
    #         name = '[' + patient['ref'] + '] ' + patient['name']
    #         patient_list.append((patient.id, name))
    #    return patient_list


    # @api.multi
    # @api.depends('name', 'ref')
    def name_get(self):
        result = []
        for record in self:
            if record.ref:
                name = '[' + record.ref + '] ' + record.name
            else:
                name = record.name
            result.append((record.id, name))
        return result


    @api.depends('name')
    def _compute_display_name(self):
        for appointment in self:
            appointment.display_name = f'[{appointment.ref}] {appointment.name} '