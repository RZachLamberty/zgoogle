#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: __init__.py
Author: zlamberty
Created: 2015-06-08

Description:
    Module for google utility functions

Usage:
    <usage>

"""

import logging
import logging.config

import auth
import gmaps
import constants


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

logger = logging.getLogger(__name__)
logging.config.dictConfig(constants.LOGCONF)
