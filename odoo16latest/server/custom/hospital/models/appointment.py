from odoo import models, fields, api, _


# Define new models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'  # Give the models name
    _inherit = ['mail.thread',
                'mail.activity.mixin']  # To inherit mailbox in record page
    _description = 'Appointment'

    @api.model
    def create(self, vals):
        if vals.get('name', _("New")) == _("New"):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _("New")
        result = super(HospitalAppointment, self).create(vals)
        return result
    name = fields.Char(string='Appointment ID', required=True, copy=False,
                           readonly=True, index=True,
                           default=lambda self: _('New') ,related='patient_id.name_seq')  # To add sequence number foe each patient record
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer(string='Age', related='patient_id.patient_age')
    notes = fields.Text(string='Registration Notes')
    appointment_date = fields.Date(string='Date', required=True)

