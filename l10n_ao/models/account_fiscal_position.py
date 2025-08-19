# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    l10n_ao_fp_type = fields.Selection(
        selection=[
            ('domestic', 'Domestic'),
            ('export', 'Export'),
            ('import', 'Import'),
            ('exempt', 'Exempt'),
        ],
        string='Angola Fiscal Position Type',
        default='domestic',
    )

    @api.model
    def _get_fiscal_position(self, partner, delivery=None):
        if not delivery:
            delivery = partner

        if self.env.company.country_id.code != "AO" or delivery.country_id.code != 'AO':
            return super()._get_fiscal_position(partner, delivery=delivery)

        # manually set fiscal position on partner has a higher priority
        manual_fiscal_position = delivery.property_account_position_id or partner.property_account_position_id
        if manual_fiscal_position:
            return manual_fiscal_position

        # Default to domestic for Angolan companies
        return self.search([('l10n_ao_fp_type', '=', 'domestic'), ('company_id', '=', self.env.company.id)], limit=1)
