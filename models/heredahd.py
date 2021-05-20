# -*- coding: utf-8 -*-
from odoo import models, fields, api

class heredaHD(models.Model):
    _inherit = "helpdesk.ticket"

    cat1 = fields.Many2one("practicauno_cat1")
    cat2 = fields.Many2one("practicauno_cat2", domain = "[('relCat1','=',cat1)]")
    cat3 = fields.Many2one("practicauno_cat3", domain = "[('relCat2','=',cat2)]")
    cat4 = fields.Many2one("practicauno_cat4", domain = "[('relCat3','=',cat3)]")