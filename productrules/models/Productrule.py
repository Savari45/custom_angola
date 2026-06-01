from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class ProductCodeMaster(models.Model):
    _name = 'product.code.master'
    _description = 'Product Code Master'
    _rec_name = 'display_name'

    name = fields.Char(
        string='Product Code',
        required=True
    )

    product_name = fields.Char(
        string='Product Name'
    )

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True
    )

    product_tmpl_ids = fields.One2many(
        'product.template',
        'product_code_id',
        string='Products'
    )

    @api.depends('name', 'product_name')
    def _compute_display_name(self):
        for rec in self:
            if rec.product_name:
                rec.display_name = f"{rec.name} - {rec.product_name}"
            else:
                rec.display_name = rec.name

    def name_get(self):
        res = []
        for rec in self:
            if rec.product_name:
                res.append((rec.id, f"{rec.name} - {rec.product_name}"))
            else:
                res.append((rec.id, rec.name))
        return res

    def write(self, vals):
        # Prevent modification of name or product_name after creation
        if 'name' in vals or 'product_name' in vals:
            raise UserError("You cannot modify Product Code or Product Name after creation!")
        return super(ProductCodeMaster, self).write(vals)
    @api.constrains('name')
    def _check_duplicate_product_code(self):
        for rec in self:
            if rec.name:
                existing_code = self.search([
                    ('id', '!=', rec.id),
                    ('name', '=', rec.name)
                ], limit=1)
                if existing_code:
                    raise ValidationError(
                        f"Product Code already exists!\nExisting: {existing_code.name} - {existing_code.product_name or 'No Product Name'}"
                    )

    @api.onchange('name')
    def _onchange_duplicate_product_code(self):
        if self.name:
            existing_code = self.search([
                ('id', '!=', self.id),
                ('name', '=', self.name)
            ], limit=1)
            if existing_code:
                self.name = False
                message = f"Product Code already exists!\nExisting: {existing_code.name} - {existing_code.product_name or 'No Product Name'}"
                return {
                    'warning': {
                        'title': 'Warning',
                        'message': message
                    }
                }




class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_code_id = fields.Many2one(
        'product.code.master',
        string='Product Code',
        required=True,
        copy=False
    )
    product_code_name = fields.Char(
        related='product_code_id.name',
        string='Product Code',
        store=True,
        readonly=True
    )

    @api.onchange('name')
    def _onchange_name(self):
        if self.name and not self.product_code_id:
            self.name = False
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'Please select Product Code first.'
                }
            }

    @api.onchange('product_code_id')
    def _onchange_product_code_id(self):
        if self.product_code_id:
            # Copy product_name to product.template name
            if self.product_code_id.product_name:
                self.name = self.product_code_id.product_name

    @api.constrains('product_code_id')
    def _check_unique_product_code(self):
        for record in self:
            if record.product_code_id:
                existing = self.search([
                    ('id', '!=', record.id),
                    ('product_code_id', '=', record.product_code_id.id)
                ], limit=1)
                if existing:
                    raise ValidationError(
                        f"This Product Code is already used by another product!\nExisting Product: {existing.name} (Code: {existing.product_code_id.name})"
                    )

    @api.constrains('name')
    def _check_unique_product(self):
        for record in self:
            existing_product = self.search([
                ('id', '!=', record.id),
                ('name', '=', record.name)
            ], limit=1)
            if existing_product:
                raise ValidationError(
                    f"Product name already exists!"
                )


    @api.model
    def copy(self, default=None):
        raise UserError(
            "Duplicating products is not allowed."
        )


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_code_id = fields.Many2one(
        related='product_tmpl_id.product_code_id',
        store=True,
        readonly=False
    )
    product_code_name = fields.Char(
        related='product_code_id.name',
        string='Product Code',
        store=True,
        readonly=True
    )

    @api.model
    def copy(self, default=None):
        raise UserError(
            "Duplicating products is not allowed."
        )

