# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://devintellecs.com>).
#
##############################################################################
#
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
from datetime import datetime, timedelta

class account_account(models.Model):
    _inherit = 'account.account'
    
    
    is_discount = fields.Boolean("Discount Account", default=False,help="Is the account for discount in move line",copy=False)
    
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
    
    
        
