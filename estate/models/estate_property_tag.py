from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property.tag"
    _description = "???"

    name = fields.Char(required=True)
    