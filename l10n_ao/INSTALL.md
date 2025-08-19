# Installation Guide for Angola Localization Package (l10n_ao)

## Prerequisites

- Odoo 18.0 or later
- Accounting module installed
- Company configured with Angola as country

## Installation Steps

### 1. Automatic Installation (Recommended)

The module will be automatically installed when:
- The Accounting module is installed
- The company's country is set to Angola (AO)

### 2. Manual Installation

1. **Copy the module** to your Odoo addons directory
2. **Update the addons list** in Odoo
3. **Install the module** from the Apps menu
4. **Configure your company** with Angola as country

## Configuration

### Company Setup

1. Go to **Settings > Companies > Companies**
2. Select your company
3. Set **Country** to Angola
4. Set **Currency** to Angolan Kwanza (AOA)
5. Save the changes

### Chart of Accounts

The chart of accounts will be automatically configured with:
- 6-digit account numbering system
- Portuguese account names
- Standard categories: Assets, Liabilities, Equity, Revenue, Cost of Sales, Expenses

### Tax Configuration

IVA taxes are pre-configured:
- **Standard Rate**: 14%
- **Reduced Rate**: 5%
- **Zero Rate**: 0%
- **Exempt**: Financial services, education, healthcare

### Fiscal Positions

Four fiscal positions are available:
- **Domestic**: For transactions within Angola
- **Export**: For exports (0% IVA)
- **Import**: For imports
- **Exempt**: For exempt transactions

## Verification

After installation, verify:

1. **Chart of Accounts** is loaded with Portuguese names
2. **Taxes** are configured with correct IVA rates
3. **Fiscal Positions** are available
4. **Reports** show Angola-specific information

## Troubleshooting

### Common Issues

1. **Module not found**: Ensure the module is in the addons directory
2. **Chart not loading**: Check company country is set to Angola
3. **Tax errors**: Verify tax configurations in the data files

### Error Logs

Check Odoo logs for specific error messages:
```bash
tail -f /var/log/odoo/odoo.log
```

## Support

For issues or questions:
1. Check the README.md file
2. Review Odoo documentation
3. Contact your Odoo partner

## Uninstallation

To uninstall:
1. Go to **Apps** menu
2. Find "Angola - Accounting"
3. Click **Uninstall**

**Note**: Uninstalling will remove all Angola-specific configurations.
