from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'

    
    confirmed_user_id = fields.Many2one(
        string='Confirmed User',
        comodel_name='res.users'
    )
    
    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        print("Success..............................")
        self.confirmed_user_id = self.env.user.id
        