from datetime import date
from odoo import api, fields, models

class CancelAppointment(models.TransientModel):
    _name = "cancel.appointment.wizard"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointment, self).default_get(fields)
        res['date_cancel'] = date.today()
        res['appointment_id'] = self.env.context.get('active_id')
        return res
        
    
        
    _description = "Cancel Appointment Wizard"
    _rec_name = "appointment_id"

    appointment_id = fields.Many2one(
        string='Appointment',
        comodel_name='hospital.appointment'
    )
    
    reason = fields.Text(string='Reason')

    
    date_cancel = fields.Date(
        string='Date Cancel',
    )
    
    def action_cancel(self):
        
        self.mapped('appointment_ids').write({'state': 'cancel'})
        print("Action Cancel in cancel appointment .........")
        
        # # Retrieve the active appointment based on the context
        # appointment_id = self.env['hospital.appointment'].search([('id', '=', self.env.context.get('active_id'))])
        
        # # Ensure that exactly one record is found
        # if appointment_id:
        #     appointment_id.write({'state': 'cancel'})
        # else:
        #     print("No appointment found with the provided ID.")
        
        # return

