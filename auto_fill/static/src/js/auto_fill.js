/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useInputField } from "@web/views/fields/input_field_hook";
import { _t } from "@web/core/l10n/translation";
import { Component, useRef, onWillUpdateProps } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { rpc } from "@web/core/network/rpc";

export class FieldAutoFill extends Component {
    static template = 'FieldAutoFill'

    setup() {
        super.setup();
        this.orm = useService("orm");
        this.input = useRef('input_data');

        // Initialize with current record value
        this.currentValue = this.props.record.data[this.props.name] || "";

        // Update when props change (record navigation)
        onWillUpdateProps((nextProps) => {
            if (nextProps.record.data[this.props.name] !== this.currentValue) {
                this.currentValue = nextProps.record.data[this.props.name] || "";
                if (this.input.el) {
                    this.input.el.value = this.currentValue;
                }
                this.hideDropdown();
            }
        });

        useInputField({
            getValue: () => this.currentValue,
            setValue: (value) => {
                this.currentValue = value;
                this.props.record.update({ [this.props.name]: value });
            },
            refName: "input_data"
        });
    }

    hideDropdown() {
        const dropdown = this.input.el?.nextSibling;
        if (dropdown) {
            dropdown.style.display = 'none';
        }
    }

    _onKeyup(ev) {
        const value = ev.target.value;
        this.currentValue = value;

        // Remove the minimum character check to show dropdown on first character
        if (!value) {
            this.hideDropdown();
            return;
        }

        const model = this.props.record.resModel;
        const fieldType = this.props.record.fields[this.props.name].type;

        if (fieldType === "char") {
            rpc('/matching/records', {
                model: model,
                field: this.props.name,
                value: value,
            }).then((result) => {
                this.updateDropdown(result);
            });
        } else {
            this.env.model.dialog.add(AlertDialog, {
                body: _t("Only supported for 'char' type. Please change field type to 'char'."),
            });
        }
    }

    updateDropdown(results) {
        const dropdown = this.input.el.nextSibling;

        // Clear existing rows
        dropdown.innerHTML = '';

        if (results && results.length > 0) {
            dropdown.style.display = 'block';

            // Remove duplicates
            const uniqueResults = [...new Set(results)];

            uniqueResults.forEach((item) => {
                const row = dropdown.insertRow();
                const cell = row.insertCell(0);
                cell.textContent = item;
            });
        } else {
            this.hideDropdown();
        }
    }

    _onTableRowClicked(ev) {
        if (ev.target.tagName === 'TD') {
            const newValue = ev.target.textContent;
            this.currentValue = newValue;
            this.input.el.value = newValue;
            this.props.record.update({ [this.props.name]: newValue });
            this.hideDropdown();
        }
    }
}

FieldAutoFill.props = {
    ...standardFieldProps,
};

export const Fieldautofill = {
    component: FieldAutoFill,
    supportedTypes: ["char"],
};

registry.category("fields").add("auto_fill", Fieldautofill);