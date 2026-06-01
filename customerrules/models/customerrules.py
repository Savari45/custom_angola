from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CustomerCodeMaster(models.Model):
    _name = 'customer.code.master'
    _description = 'Customer Code Master'
    _rec_name = 'display_name'

    name = fields.Char(
        string='Customer Code',
        required=True
    )

    customer_name = fields.Char(
        string='Customer Name'
    )

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True
    )
    customer_ids = fields.One2many(
        'res.partner',
        'customer_code_id',
        string='customer codes',
    )

    @api.depends('name', 'customer_name')
    def _compute_display_name(self):
        for rec in self:
            if rec.customer_name:
                rec.display_name = f"{rec.name} - {rec.customer_name}"
            else:
                rec.display_name = rec.name

    def name_get(self):
        res = []
        for rec in self:
            if rec.customer_name:
                res.append((rec.id, f"{rec.name} - {rec.customer_name}"))
            else:
                res.append((rec.id, rec.name))
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            args = ['|', ('name', operator, name), ('customer_name', operator, name)] + args
        return self.search(args, limit=limit).name_get()


class CustomerTemplate(models.Model):
    _inherit = 'res.partner'

    customer_code_id = fields.Many2one('customer.code.master', string="Customer Code", required=True, copy=False)
    customer_code_name = fields.Char(related='customer_code_id.name', string='Customer Code', store=True, readonly=True)

    @api.onchange('vat')
    def _checkvatid(self):
        for rec in self:
            if rec.vat:
                existing_vat = self.env['res.partner'].search([('vat', '=', rec.vat), ('id', '!=', rec.id)])
                if existing_vat:
                    raise ValidationError("VAT ID already exists")

    @api.onchange('name')
    def _onchange_name(self):
        if self.name and not self.customer_code_id:
            self.name = False
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'Please select customer Code first.'
                }
            }

    @api.onchange('customer_code_id')
    def _onchange_customer_code_id(self):
        if self.customer_code_id:
            # Copy customer_name to res.partner name
            if self.customer_code_id.customer_name:
                self.name = self.customer_code_id.customer_name

    @api.constrains('customer_code_id')
    def _check_unique_customer_code_id(self):
        for record in self:
            if record.customer_code_id:
                existing = self.search([
                    ('id', '!=', record.id),
                    ('customer_code_id', '=', record.customer_code_id.id)
                ], limit=1)
                if existing:
                    raise ValidationError(
                        f"This Customer Code is already used by another customer!\nExisting Customer: {existing.name} (Code: {existing.customer_code_id.name})"
                    )

    @api.constrains('name')
    def _check_unique_customer(self):
        for record in self:
            existing_customer = self.search([
                ('id', '!=', record.id),
                ('name', '=', record.name)
            ], limit=1)
            if existing_customer:
                raise ValidationError(
                    f"Customer name already exists!"
                )
