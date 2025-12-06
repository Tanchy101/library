# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################
    _inherit = "library.book"
    _description = "Book Extended"

    ###################
    # Default methods #
    ###################
   
    author_id = fields.Many2one(string="Author",
                          required=True,
                          comodel_name="res.partner")
    
    category_id = fields.Many2many(string="Category",
                                   comodel_name="library.book.category")

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
