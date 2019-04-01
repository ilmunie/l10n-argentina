###############################################################################
#   Copyright (c) 2018 Eynes/E-MIPS (Gaston Alberto Bertolani)
#   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
###############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountFiscalReport(models.TransientModel):
    _name = "account.fiscal.report"

    report_config_id = fields.Many2one('account.fiscal.report.config',
            'Config', required=True)
    period_id = fields.Many2one('date.period', 'Period')

    @api.multi
    def generate_report(self):
        report_type = self.report_config_id.report_type
        function_name = '_execute_' + report_type
        res = {}
        if hasattr(self, function_name):
            function = getattr(self, function_name)
            res = function()
        return res
