from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_code = fields.Char(
        string='Product Code',
        help='Enter a Product Code'
    )

    @api.constrains('name', 'product_code')
    def _check_unique_product(self):

        for record in self:

            # Product Name Validation
            if record.name:

                existing_product = self.search([
                    ('id', '!=', record.id),
                    ('name', '=', record.name)
                ], limit=1)

                if existing_product:
                    raise ValidationError(
                        "Product name already exists!"
                    )

            # Product Code Validation
            if record.product_code:

                existing_code = self.search([
                    ('id', '!=', record.id),
                    ('product_code', '=', record.product_code)
                ], limit=1)

                if existing_code:
                    raise ValidationError(
                        "Product code already exists!"
                    )

    @api.model
    def copy(self, default=None):
        raise UserError(
            "Duplicating products is not allowed."
        )


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_code = fields.Char(
        related='product_tmpl_id.product_code',
        store=True,
        readonly=False
    )

    @api.model
    def copy(self, default=None):
        raise UserError(
            "Duplicating products is not allowed."
        )

    """        
    @api.onchange('default_code')
    def _check_unique_productid(self):
        for record in self:
            if record.default_code:
                existing_product1 = self.env['product.template'].search([('default_code', '=', record.default_code)])
                if existing_product1:
                    raise ValidationError("A product with the same product ID and internal reference already exists!")
    
   @api.constrains('name', 'default_code')
    def _check_unique_product(self):
        for record in self:
            if record.name and record.default_code:
                existing_product = self.env['product.template'].search([
                    ('id', '!=', record.id),
                    ('name', '=', record.name),
                    ('default_code', '=', record.default_code)
                ])
                if existing_product:
                    raise ValidationError("A product with the same name and internal reference already exists!")

    """