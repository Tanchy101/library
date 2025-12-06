# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBookCategory(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book.category"
    _description = "Book Category"

    ###################
    # Default methods #
    ###################
   
    name  = fields.Char(string="Category",
                          required=True)
    
    _sql_constraints = [('unique_name', 'unique(name)', "Category already exists!")]

    ######################
    # Fields declaration #
    ######################

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
