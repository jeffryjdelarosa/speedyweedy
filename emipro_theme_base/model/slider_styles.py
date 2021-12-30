# -*- coding: utf-8 -*-
"""
    This model is used to create a slider styles fields
"""
from odoo import api, fields, models, _

class SliderStyles(models.Model):
    _name = "slider.styles"
    _description = "Slider Styles"

    name = fields.Char(string='Name', required=True)
    # theme_id = fields.Many2one('ir.module.module', string="Theme", required=True)
    theme_id = fields.Many2one('ir.module.module', string="Theme")
    # theme_id = fields.Many2one('ir.module.module', help='Installed theme')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        website = self.env['website'].get_current_website()
        domain = [('theme_id', '=', website.theme_id.id)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)