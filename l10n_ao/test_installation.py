#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for Angola Localization Package (l10n_ao)
This script helps verify that the package is properly installed and configured.
"""

import os
import sys

def test_file_structure():
    """Test if all required files are present."""
    print("🔍 Testing file structure...")
    
    required_files = [
        '__init__.py',
        '__manifest__.py',
        'README.md',
        'INSTALL.md',
        'models/__init__.py',
        'models/template_ao.py',
        'models/account_fiscal_position.py',
        'data/account.account.tag.csv',
        'data/account_tax_report_data.xml',
        'data/menuitem_data.xml',
        'data/chart_template_data.xml',
        'data/fiscal_position_data.xml',
        'data/account_group_data.xml',
        'data/template/account.account-ao.csv',
        'data/template/account.tax.group-ao.csv',
        'data/template/account.tax-ao.csv',
        'demo/demo_company.xml',
        'i18n/pt.po',
        'static/description/index.html',
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files are present")
        return True

def test_manifest():
    """Test if the manifest file is valid."""
    print("🔍 Testing manifest file...")
    
    try:
        with open('__manifest__.py', 'r') as f:
            content = f.read()
            
        # Check for required fields
        required_fields = ['name', 'category', 'depends', 'data']
        missing_fields = []
        
        for field in required_fields:
            if field not in content:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Missing manifest fields: {missing_fields}")
            return False
        else:
            print("✅ Manifest file is valid")
            return True
            
    except Exception as e:
        print(f"❌ Error reading manifest: {e}")
        return False

def test_csv_files():
    """Test if CSV files are properly formatted."""
    print("🔍 Testing CSV files...")
    
    csv_files = [
        'data/account.account.tag.csv',
        'data/template/account.account-ao.csv',
        'data/template/account.tax.group-ao.csv',
        'data/template/account.tax-ao.csv',
    ]
    
    for csv_file in csv_files:
        try:
            with open(csv_file, 'r') as f:
                lines = f.readlines()
                
            if len(lines) < 2:  # Header + at least one data row
                print(f"❌ {csv_file} has insufficient data")
                return False
                
            # Check for False values that could cause issues
            content = ''.join(lines)
            if 'False' in content:
                print(f"❌ {csv_file} contains 'False' values that may cause issues")
                return False
                
        except Exception as e:
            print(f"❌ Error reading {csv_file}: {e}")
            return False
    
    print("✅ CSV files are properly formatted")
    return True

def test_xml_files():
    """Test if XML files are properly formatted."""
    print("🔍 Testing XML files...")
    
    xml_files = [
        'data/account_tax_report_data.xml',
        'data/menuitem_data.xml',
        'data/chart_template_data.xml',
        'data/fiscal_position_data.xml',
        'data/account_group_data.xml',
    ]
    
    for xml_file in xml_files:
        try:
            with open(xml_file, 'r') as f:
                content = f.read()
                
            # Basic XML validation
            if not content.strip().startswith('<?xml'):
                print(f"❌ {xml_file} is not a valid XML file")
                return False
                
        except Exception as e:
            print(f"❌ Error reading {xml_file}: {e}")
            return False
    
    print("✅ XML files are properly formatted")
    return True

def main():
    """Main test function."""
    print("🇦🇴 Testing Angola Localization Package (l10n_ao)")
    print("=" * 50)
    
    tests = [
        test_file_structure,
        test_manifest,
        test_csv_files,
        test_xml_files,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The package is ready for installation.")
        return 0
    else:
        print("⚠️  Some tests failed. Please fix the issues before installation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
