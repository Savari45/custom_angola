from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomerTemplate(models.Model):
    _inherit = 'res.partner'

    customercode=fields.Char(string='Customer Code')


    @api.onchange('vat')
    def _checkvatid(self):
        for rec in self:
            if rec.vat:
                exiting_vat=self.env['res.partner'].search([('vat','=',rec.vat)])
                if exiting_vat:
                   raise ValidationError("VAT ID already exisit")