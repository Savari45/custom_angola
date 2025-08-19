# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ao')
    def _get_ao_template_data(self):
        return {
            'name': 'Plano de Contas Angola',
            'code_digits': '6',
            # 'property_account_receivable_id': 'ao_31121',
            # 'property_account_payable_id': 'ao_32121',
            # 'property_account_expense_categ_id': 'ao_2121',
            # 'property_account_income_categ_id': 'ao_6111',
            # 'property_stock_account_input_categ_id': 'ao_200000',
            # 'property_stock_account_output_categ_id': 'ao_100000',
            # 'property_stock_valuation_account_id': 'ao_120000',
        }

    @template('ao', 'res.company')
    def _get_ao_res_company(self):
        return {
            self.env.company.id: {
                'anglo_saxon_accounting': True,
                'account_fiscal_country_id': 'base.ao',
                'bank_account_code_prefix': '1200',
                'cash_account_code_prefix': '1250',
                'transfer_account_code_prefix': '1010',
                # 'account_default_pos_receivable_account_id': 'ao_110010',
                # 'income_currency_exchange_account_id': 'ao_500100',
                # 'expense_currency_exchange_account_id': 'ao_610100',
                # 'account_journal_early_pay_discount_loss_account_id': 'ao_610200',
                # 'account_journal_early_pay_discount_gain_account_id': 'ao_500200',
                # 'default_cash_difference_income_account_id': 'ao_500300',
                # 'default_cash_difference_expense_account_id': 'ao_610300',
                # 'account_sale_tax_id': 'ao_iva_venda_14',
                # 'account_purchase_tax_id': 'ao_iva_compra_14',
                # 'fiscalyear_last_day': '31',
                # 'fiscalyear_last_month': '12',
            },
        }
