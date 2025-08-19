# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Angola - Accounting',
    'icon': '/l10n_ao/static/description/icon.png',
    'countries': ['ao'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the basic Angola localisation necessary to run Odoo in Angola:
====================================================================

    - Chart of Accounts (Plano de Contas)
    - Tax structure for Angola (IVA - Imposto sobre o Valor Acrescentado)
    - Fiscal positions for domestic and international transactions
    - Company template configuration
    - Currency: Angolan Kwanza (AOA)
    """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/documentation/master/applications/finance/fiscal_localizations.html',
    'depends': [
        'account',
        'base_vat',
    ],
    'auto_install': ['account'],
    'data': [
        # 'data/l10n_ao_chart_data.xml',
        # 'data/account_tax_data.xml',
        'data/res_country_states.xml',
        # 'data/account_fiscal_position_template_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
