# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.model):
    _inherit = 'sale.order'

    x = fields.Char()
