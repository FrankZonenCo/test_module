from odoo import models, fields

class MijnModel(models.Model):
    _name = 'test.module'
    _description = 'Beschrijving van mijn model'

    name = fields.Char(string='Naam', required=True)
    description = fields.Text(string='Beschrijving')
