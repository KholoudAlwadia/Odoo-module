# Inherit models from odoo


from odoo import models, fields, api, _


# Inherit model from existing model
class InheritModel(models.Model):
    # Give the  models name
    _inherit = 'sale.order'
    patient_name = fields.Char(string='Patient Name')

# Define new models


class HospitalPatient(models.Model):
    # Give the  models name
    _name = 'hospital.patient'
    # To inherit mailbox in record page
    _inherit = ['mail.thread',
                'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'  # To Write patient name in record rather than field name and id number in record title

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    patient_name = fields.Char(string='Name', required=True, track_visibility="always")
    patient_age = fields.Integer(string='Age', track_visibility="always")
    notes = fields.Text(string='Notes', track_visibility="always")
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False,
                           readonly=True, index=True,
                           default=lambda self: _('New'))  # To add sequence number foe each patient record
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='female', string='Gender')
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')], string='Age Group', compute='set_age_group')

    # To create new sequence number for each patient record
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _("New")) == _("New"):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _("New")
        result = super(HospitalPatient, self).create(vals)
        return result










