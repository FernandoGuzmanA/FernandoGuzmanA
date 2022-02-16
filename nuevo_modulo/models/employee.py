# -*- coding: utf-8 -*-

from odoo import models, fields


class Employee(models.Model):
    _name = 'employee'
    _description = 'hola mundo'

    image = fields.Binary(
        string='Image',
    )
    name = fields.Char(
        string='Name',
        size=64,
        required=True,
        readonly=False
    )
    value = fields.Integer(
        string='Age'
    )
    value2 = fields.Float(
        string='Height'
    )
    description = fields.Text(
        string='Description'
    )
    # leader_id = fields.Many2one(
    #     string='Leader',
    #     comodel_name='leader',
    #     required='True'
    # )

    leader_ids = fields.Many2many(
        'leader',
        'employee_leader_rel',
        'employee_id',
        'leader_id'
    )
