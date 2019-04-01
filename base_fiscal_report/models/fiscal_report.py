###############################################################################
#   Copyright (c) 2018 Eynes/E-MIPS (Gaston Alberto Bertolani)
#   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
###############################################################################

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountFiscalReportConfig(models.Model):
    _name = "account.fiscal.report.config"
    _description = "Fiscal Report Config"

    name = fields.Char('Name')
    report_type = fields.Selection([], required=True)


class ResPartnerAdvanceRetention(models.Model):
    _name = "account.fiscal.report.files"
    _description = "Fiscal Report Files"

    name = fields.Char("Reference")
    report_config_id = fields.Many2one('account.fiscal.report.config', 'Configuration', required=True)
    period_id = fields.Many2one('date.period', 'Period')
    state = fields.Selection([
        ('new', 'New'),
        ('error', 'With Error'),
        ('presented', 'Presented')
    ], string='State', dafault='new')
