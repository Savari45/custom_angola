/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Many2OneField } from "@web/views/fields/many2one/many2one_field";
import { computeM2OProps, Many2One } from "@web/views/fields/many2one/many2one";

class CustomerCodeMany2One extends Many2One {
    static template = "web.Many2One";
    
    get displayName() {
        if (this.props.value) {
            // If we have the name field, use it
            if (this.props.value.name) {
                return this.props.value.name;
            }
            // Fallback to display_name
            return this.props.value.display_name?.split(" - ")[0] || this.props.value.display_name || "";
        }
        return "";
    }
}

class CustomerCodeMany2OneField extends Many2OneField {
    static components = { Many2One: CustomerCodeMany2One };
    
    get m2oProps() {
        const props = computeM2OProps(this.props);
        // Make sure we fetch the 'name' field from CustomerCodeMaster
        props.specification = { name: {}, display_name: {} };
        return props;
    }
}

registry.category("fields").add("customer_code_display", {
    ...registry.category("fields").get("many2one"),
    component: CustomerCodeMany2OneField,
});
