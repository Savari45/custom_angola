from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Producttemplate(models.Model):
    _inherit = 'product.template'

    #_sql_constraints = {
    #   ('unique_name', 'unique(name)', 'The Product name already exisit'),
    #                   }

    # Alternatively, for more complex logic or multiple fields:
    # @api.constrains('name','default_code')
    @api.onchange('name','default_code')
    def _check_unique_product(self):
        for record in self:
            if record.name:
                existing_product = self.env['product.template'].search([('name', '=', record.name)])
                if existing_product:
                    raise UserError("A product name already exists!")

            if record.default_code:
                existing_default_code = self.env['product.template'].search([('default_code', '=', record.default_code)])
                if existing_default_code:
                    raise ValidationError("A product id already exists!")

    @api.model
    def copy(self, default=None):
        raise UserError("Duplicating products is not allowed.")


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