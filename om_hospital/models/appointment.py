from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "ref"

    patient_id = fields.Many2one(
        string='Patients',
        comodel_name='hospital.patient'
    )
    
    appointment_time = fields.Datetime(
        string='Appointment Time',
        default=fields.Datetime.now,
    )
    
    
    booking_date = fields.Date(
        string='Booking Date',
        default=fields.Date.context_today,
    )
            
    gender = fields.Selection(
        related='patient_id.gender', 
        # selection=[('male', 'Male'), ('female', 'Female')], # readonly=False, tracking=True,
    )    

    ref = fields.Char(
        string='Reference', help='Reference from record') # related='patient_id.ref')
    
    prescription = fields.Html(
        string='Prescription'
    )
    priority = fields.Selection([
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Very High')], string="Priority")
            
    
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('in_consultation', 'In Consultation'),  ('done', 'Done'),  ('cancel', 'Cancel')],
        default='draft',
        readonly=True,
    )
    
    def action_draft(self):
        self.state = 'draft'

    def action_done(self):
        self.state = 'done'
        # return {
        #     'effect': {
        #         'fadeout': 'slow',
        #         'message': 'Done successfully',
        #         'type': 'rainbow_man',
        #     }
        # }

    def action_in_consultation(self):
        self.state = 'in_consultation'
    
    def action_cancel(self):
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action
    
    
    priority = fields.Selection([
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Very High')], string="Priority")

    
    doctor_id = fields.Many2one(
        string='Doctor',
        comodel_name='res.users'
    )
        
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id',
        string='Pharmacy Lines'
    )

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        # for rec in self:
        self.ref = self.patient_id.ref
    

class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    qty = fields.Integer(
        string='Quantity', default="1"
    )    
    price_unit = fields.Float(
        string='Price Unit', related='product_id.list_price'
    )
    
    appointment_id = fields.Many2one('hospital.appointment')