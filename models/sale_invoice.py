# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleInvoiceLine(models.Model):
    _inherit = "account.move.line"
    _description = 'Custom field added in invoice'

    discount_amount = fields.Float(string="Discount Amount")


class UpdateCustomFieldInvoice(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
    _description = 'Update the custom field value from sale order to invoice'

    def create_invoices(self):
        res = super(UpdateCustomFieldInvoice, self).create_invoices()
        active_id = self._context.get('active_id')
        lst = []
        if active_id:
            sale_id = self.env['sale.order'].browse(active_id)
            invoice_id = self.env['account.move'].search([('invoice_origin', '=', sale_id.name)])
            lst = []
            for rec in sale_id.order_line:
                lst.append(rec.discount_amount)
            i = 0
            for val in invoice_id.invoice_line_ids:
                print(lst[i])
                val.discount_amount = lst[i]
                i += 1

            return res
