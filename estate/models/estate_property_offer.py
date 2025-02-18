from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = "estate.property.offer"
    _description = "???"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7)
    create_date = fields.Date(default=lambda self: fields.Date.today())
    date_deadline = fields.Date(compute="_compute_date_deadline",
                                inverse="_inverse_date_deadline")

    @api.depends('create_date','validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.add(record.create_date,days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.today()

    @api.onchange('date_deadline')
    def _onchange_validity(self):
        self.validity = (self.date_deadline - self.create_date).days
        if self.validity < 0: self.validity = 0