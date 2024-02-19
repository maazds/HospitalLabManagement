from odoo import fields,api,models

class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Doctor select and enter patient info and send it to the lab'

    PatientName = fields.Char('Patient Name')
    PatientSex = fields.Selection([('male','Male'),('female','Female'),('other','Other')],'Sex')
    PatientDOB = fields.Date('Date of Birth')
    PatientAge = fields.Char('Age')