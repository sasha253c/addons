# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'FP/POS Hardware Driver',
    'version': '1.0',
    'category': 'Hardware Drivers',
    'sequence': 6,
    'website': 'https://www.odoo.com/page/point-of-sale',
    'summary': 'Hardware Driver for FP/POS Printers and Cashdrawers from Datecs (ICL)',
    'description': """
FP/POS Hardware Driver
=======================

This module allows openerp to print with FP/POS compatible printers and
to open FP/POS controlled cashdrawers in the point of sale and other modules
that would need such functionality.

""",
    'author': 'Rosen Vladimirov',
    'depends': ['hw_proxy'],
    'external_dependencies': {
        'python' : ['usb.core','serial','qrcode'],
    },
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
