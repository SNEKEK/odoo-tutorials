from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property.offer"
    _description = "???"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)