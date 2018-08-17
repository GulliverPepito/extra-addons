# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Movimiento(models.Model):
    _name = "sa.movimiento"

    name = fields.Char(string="Descripción")
    monto = fields.Float(string="Monto")
    tipo = fields.Selection(selection=[("I","Ingreso"),("G","Gasto")])
    fecha = fields.Date(string="Fecha")
    comprobante = fields.Binary(string="Imagen de Comprobante")

# class extra-addons/saldoapp(models.Model):
#     _name = 'extra-addons/saldoapp.extra-addons/saldoapp'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100