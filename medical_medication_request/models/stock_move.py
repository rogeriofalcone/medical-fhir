# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = 'stock.picking'

    medication_administration_id = fields.Many2one(
        comodel_name='medical.medication.administration',
        string='Medication administration event',
        ondelete='restrict', index=True,
    )
