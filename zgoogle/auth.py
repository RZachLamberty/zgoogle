#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: auth.py
Author: zlamberty
Created: 2015-06-08

Description:
    Module for google api authentication functions

Usage:
    <usage>

"""

import logging
import yaml


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

logger = logging.getLogger(__name__)


# ----------------------------- #
#   authentication helpers      #
# ----------------------------- #

class ZgoogleAuthError(Exception):
    pass


def load_auth_yaml(f):
    """ load a yaml file that should contain keys 'api_key'. """
    with open(f, 'rb') as fIn:
        d = yaml.load(fIn)
    if not 'api_key' in d:
        raise ZgoogleAuthError(
            "yaml file improperly formatted; requires 'api_key'"
        )
    return d
