# Angola - Fiscal Localization Package (l10n_ao)

This module provides comprehensive fiscal localization for companies operating in Angola, implementing the country's specific accounting and tax requirements.

## 🇦🇴 Features

### Chart of Accounts
- **Complete Portuguese chart of accounts** following Angolan accounting standards
- **6-digit account codes** for detailed financial tracking
- **Standard account categories**: Assets, Liabilities, Equity, Revenue, Cost of Sales, Expenses
- **Reconcilable accounts** for bank, customers, and suppliers

### Tax Structure (IVA - Imposto sobre o Valor Acrescentado)
- **Standard IVA Rate**: 14% (most goods and services)
- **Reduced IVA Rate**: 5% (basic food items, books, medicines)
- **Zero Rate**: 0% (exports, international services)
- **Exempt**: Financial services, education, healthcare
- **Stamp Duty**: 0.5% on certain transactions
- **Income Tax**: 10% withholding on certain payments

### Fiscal Compliance
- **Tax reports** for IVA declarations
- **Fiscal positions** for domestic and international transactions
- **Company template** with Angolan-specific settings
- **Currency support** for Angolan Kwanza (AOA)

## 📁 Package Structure

```
l10n_ao/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   └── template_ao.py
├── data/
│   ├── account.account.tag.csv
│   ├── account_tax_report_data.xml
│   ├── menuitem_data.xml
│   └── template/
│       ├── account.account-ao.csv
│       ├── account.tax.group-ao.csv
│       └── account.tax-ao.csv
├── demo/
│   └── demo_company.xml
├── i18n/
│   └── pt.po
└── static/
    └── description/
        └── index.html
```

## 🚀 Installation

1. **Automatic Installation**: This module will be automatically installed when the Accounting module is installed for companies based in Angola.

2. **Manual Installation**: 
   - Copy the `l10n_ao` folder to your Odoo addons directory
   - Update the addons list in Odoo
   - Install the module from the Apps menu

## ⚙️ Configuration

### Company Setup
- Set country to Angola
- Currency will automatically be set to Angolan Kwanza (AOA)
- Chart of accounts will be automatically configured

### Tax Configuration
- IVA taxes are pre-configured with correct rates
- Tax accounts are automatically linked
- Fiscal positions are set up for common scenarios

### Chart of Accounts
- 6-digit account numbering system
- Portuguese account names
- Reconcilable accounts for bank, customers, and suppliers

## 📊 Tax Rates

| Tax Type | Rate | Description |
|----------|------|-------------|
| IVA Standard | 14% | Most goods and services |
| IVA Reduced | 5% | Basic food, books, medicines |
| IVA Zero | 0% | Exports, international services |
| IVA Exempt | 0% | Financial services, education, healthcare |
| Stamp Duty | 0.5% | Certain transactions |
| Income Tax | 10% | Withholding on certain payments |

## 🔧 Technical Details

### Dependencies
- `account`: Core accounting module
- `base_vat`: VAT validation support

### Auto-install
- Automatically installed when `account` module is installed for Angolan companies

### Data Files
- **Chart of Accounts**: 70+ accounts with Portuguese names
- **Tax Groups**: IVA, Impostos, Taxas
- **Taxes**: 10 different tax configurations
- **Reports**: IVA tax reports for compliance

## 🌍 Language Support

- **Primary Language**: Portuguese (Angola) - pt_AO
- **Account Names**: All in Portuguese
- **Tax Names**: Portuguese terminology
- **Reports**: Portuguese labels

## 📋 Compliance

This package implements:
- Angolan chart of accounts structure
- IVA tax requirements
- Fiscal reporting standards
- Company registration requirements

## 🤝 Contributing

To contribute to this localization package:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For technical support:
- Check the Odoo documentation
- Contact your Odoo partner
- Review the module's description page in Odoo

## 📄 License

This module is licensed under LGPL-3.

## 🔄 Version History

- **1.0**: Initial release with complete Angola localization

---

**Note**: This module is designed to comply with Angolan fiscal requirements as of 2024. Always verify compliance with current local regulations and consult with local accounting professionals.
