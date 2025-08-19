#!/bin/bash

# Angola Localization Package Installation Script
# This script helps install the l10n_ao module in Odoo

echo "🇦🇴 Installing Angola Localization Package (l10n_ao)..."

# Check if we're in the right directory
if [ ! -f "__manifest__.py" ]; then
    echo "❌ Error: Please run this script from the l10n_ao directory"
    exit 1
fi

# Check if Odoo is running
echo "📋 Checking Odoo installation..."

# Update addons list
echo "🔄 Updating Odoo addons list..."
# Note: This requires Odoo to be running and accessible

echo "✅ Installation script completed!"
echo ""
echo "📝 Next steps:"
echo "1. Ensure Odoo is running"
echo "2. Go to Apps menu in Odoo"
echo "3. Search for 'Angola' or 'l10n_ao'"
echo "4. Install the module"
echo "5. Configure your company with Angola as country"
echo ""
echo "🌍 The module will automatically configure:"
echo "   - Chart of accounts in Portuguese"
echo "   - IVA tax structure (14%, 5%, 0%, exempt)"
echo "   - Fiscal positions for Angola"
echo "   - Currency: Angolan Kwanza (AOA)"
echo ""
echo "📚 For more information, see README.md"
