# -*- coding: utf-8 -*-
from odoo import models, fields, api

@api.onchange('')

class Categoria1(models.Model):
    _name = "practicauno_cat1"

    name = fields.Char(string="Categoria 1")
    active = fields.Boolean(default="true") #este campo permite archivar el modelo

class Categoria2(models.Model):
    _name = "practicauno_cat2"

    name = fields.Char(string="Categoria 2")

    relCat1 = fields.Many2one("practicauno_cat1", string="Categoria 1 Relacion")
    active = fields.Boolean(default="true")

class Categoria3(models.Model):
    _name = "practicauno_cat3"

    name = fields.Char(string="Categoria 3")

    relCat2 = fields.Many2one("practicauno_cat2", string="Categoria 2 Relacion")
    active = fields.Boolean(default="true")

class Categoria4(models.Model):
    _name = "practicauno_cat4"

    name = fields.Char(string="Categoria 4")

    relCat3 = fields.Many2one("practicauno_cat3", string="Categoria 3 Relacion")
    active = fields.Boolean(default="true")
