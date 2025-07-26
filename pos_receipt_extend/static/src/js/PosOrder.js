import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {
    export_for_printing(baseUrl, headerData) {
        const result = super.export_for_printing(...arguments);
        result.headerData = result.headerData || {};
        result.invoice_number = this.account_move_name || "";
        result.signature_code= this.account_move_code || "";

        result.headerData.invoice_no =  result.invoice_number;

        result.headerData.signature_code = result.signature_code
        const orderlines = this.get_orderlines();
        result.orderlines = orderlines.map((line) => {
            const qty = line.get_quantity();
            const price = line.get_unit_price();
            let tax_percent = 0;
            const prices = line.get_all_prices ? line.get_all_prices() : { taxesData: [] };
            if (prices.taxesData && prices.taxesData.length) {
                // Sum all tax percentages for the line
                tax_percent = prices.taxesData.reduce((acc, t) => acc + (t.tax.amount || 0), 0);
            }
            const subtotal = qty * price * (1 + tax_percent / 100);

            return {
                id: line.id,
                product_name: line.get_product().display_name,
                quantity: qty,
                unit: price,
                tax: tax_percent,
                subtotal: subtotal,
                discount: line.get_discount(),
            };
        });
        // Add partner details
        const partner = this.get_partner();
        if (partner) {
            result.headerData.customer_name = partner.name || "";
            result.headerData.customer_address = partner.contact_address || "";
            result.headerData.customer_mobile = partner.mobile || "";
            result.headerData.customer_phone = partner.phone || "";
            result.headerData.customer_email = partner.email || "";
            result.headerData.customer_vat = partner.vat || "";
        }

        console.log('POS Order order lines Details:', result.orderlines);
        console.log('result',result);
        return result;
    },
});