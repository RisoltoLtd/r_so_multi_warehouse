# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2022 RISOLTO
#
##############################################################################

{
    'name': "Risolto Sale Multi Warehouse",
    'version': '15.0.1.0',
    'category': 'Sales',
    'author': 'RISOLTO',
    'category': 'Sale',
    'summary': """This Module adds multi warehouse functionality in the the sale order""",
    'description': """
        Sales Multi warehouse
        =======================
        * Allow user to select source warehouse on each product in the sale order line.
        * Generate Delivery orders based on the warehouse selected .
        * User can see the selected warehouse on Pdf Report, Sales analysis report, Customer portal view.
    """,
    'license': 'OPL-3',
    'depends': ['sale_management', 'sale_stock'],
    'website': "www.risolto.co.uk",
    'data': [
        'views/sale_view.xml',
        'views/sale_report_template.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: