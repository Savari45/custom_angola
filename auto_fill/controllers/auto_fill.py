from odoo import http
from odoo.http import request


class AutoFill(http.Controller):
    """This is a controller for fetching data from the specific field
        from backend
        get_matching_records:
                            this function fetch data from backend and return
                            the value in res to the js
    """

    @http.route(['/matching/records'], type='json', auth="none")
    def get_matching_records(self, **kwargs):

        model = str(kwargs.get('model', ''))
        field = str(kwargs.get('field', ''))
        value = str(kwargs.get('value', ''))

        cr = request.cr

        # IMPORTANT
        res = []

        if len(value) > 0:

            # Product Name
            if model in ['product.template', 'product.product'] and field == 'name':

                query = """
                    SELECT DISTINCT name->>'en_US'
                    FROM product_template
                    WHERE name->>'en_US' ILIKE %s
                    AND active = true
                """

                cr.execute(query, ('%' + value + '%',))

                res = [row[0] for row in cr.fetchall() if row[0]]

            # Product Code
            elif model in ['product.template', 'product.product'] and field == 'product_code':

                query = """
                    SELECT DISTINCT
                        CONCAT(product_code, '-', name->>'en_US')
                    FROM product_template
                    WHERE (
                        product_code ILIKE %s
                        OR name->>'en_US' ILIKE %s
                    )
                    AND product_code IS NOT NULL
                    AND active = true
                """

                cr.execute(query, (
                    '%' + value + '%',
                    '%' + value + '%'
                ))

                res = [row[0] for row in cr.fetchall() if row[0]]

            # Customer Code
            elif model == 'res.partner' and field == 'customercode':

                query = """
                    SELECT DISTINCT
                        CONCAT(customercode, '-', name)
                    FROM res_partner
                    WHERE (
                        customercode ILIKE %s
                        OR name ILIKE %s
                    )
                    AND customercode IS NOT NULL
                    AND active = true
                """

                cr.execute(query, (
                    '%' + value + '%',
                    '%' + value + '%'
                ))

                res = [row[0] for row in cr.fetchall() if row[0]]

            # Default
            else:

                model = model.replace(".", "_")

                query = """
                    SELECT %s
                    FROM %s
                    WHERE %s::text ILIKE %s
                    GROUP BY %s
                """ % (
                    field,
                    model,
                    field,
                    '%' + value + '%',
                    field
                )

                cr.execute(query)

                res = [row[0] for row in cr.fetchall() if row[0]]

        return res