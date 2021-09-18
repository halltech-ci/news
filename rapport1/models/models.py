# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rapport1(models.Model):
    _name = 'rapport1.rapport1'
    _description = 'rapport1.rapport1'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()