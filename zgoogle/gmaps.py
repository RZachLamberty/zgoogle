#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: gmaps.py
Author: zlamberty
Created: 2015-06-08

Description:
    helper functions for google maps api

Usage:
    <usage>

"""

import logging

import googlemaps
import constants


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

logger = logging.getLogger(__name__)


# ----------------------------- #
#   lat lng functions           #
# ----------------------------- #

def lat_lng_from_city_state(key, city, state):
    """ use google maps api to get latitude and longitude for city name """
    gmaps = googlemaps.Client(key=key)
    loc = gmaps.geocode(
        "{}, {}".format(city.capitalize(), state.upper())
    )[0]['geometry']['location']
    return loc['lat'], loc['lng']


def get_google_bounding_box(key, city, state):
    """ use google maps api to get bounding box for city """
    gmaps = googlemaps.Client(key=key)
    loc = gmaps.geocode(
        "{}, {}".format(city.capitalize(), state.upper())
    )[0]['geometry']['bounds']
    yMax = loc['northeast']['lat']
    xMax = loc['northeast']['lng']
    yMin = loc['southwest']['lat']
    xMin = loc['southwest']['lng']

    return xMax, xMin, yMax, yMin
