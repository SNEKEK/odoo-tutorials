from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "tutorial"

    name = fields.Char(required=True, default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda slf: fields.Date.add(fields.Date.today(),month=3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('east', 'East'),
                   ('south', 'South'), ('west', 'West')],
                   )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('new', 'New'), ('received', 'Offer Received'),
                   ('accepted', 'Offer Accepted'), ('sold', 'Sold'),
                   ('cancelled', 'Cancelled')],
                   default='new')
    property_type_id = fields.Many2one("estate.property.type")
    buyer = fields.Many2one("res.partner", copy=False)
    salesman = fields.Many2one("res.users", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer","property_id", string="Offers")
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            if record.mapped('offer_ids.price'):
                record.best_price = max(record.mapped('offer_ids.price'))
            else: 0.00

