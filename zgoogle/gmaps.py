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

import zcache


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

logger = logging.getLogger(__name__)
GMAPS = None

# ----------------------------- #
#   connect the client          #
# ----------------------------- #

def connect(key):
    global GMAPS
    GMAPS = googlemaps.Client(key=key)


# ----------------------------- #
#   lat lng functions           #
# ----------------------------- #

def lat_lng_from_city_state(city, state):
    """ use google maps api to get latitude and longitude for city name """
    loc = GMAPS.geocode(
        "{}, {}".format(city.capitalize(), state.upper())
    )[0]['geometry']['location']
    return loc['lat'], loc['lng']


def get_google_bounding_box(city, state):
    """ use google maps api to get bounding box for city """
    loc = GMAPS.geocode(
        "{}, {}".format(city.capitalize(), state.upper())
    )[0]['geometry']['bounds']
    yMax = loc['northeast']['lat']
    xMax = loc['northeast']['lng']
    yMin = loc['southwest']['lat']
    xMin = loc['southwest']['lng']

    return xMax, xMin, yMax, yMin


# ----------------------------- #
#   direction functions         #
# ----------------------------- #

@zcache.cached('get_gmaps_directions', '/tmp/get_gmaps_directions.pkl')
def get_gmaps_directions(origin, destination, mode="transit",
                         useCache=True):
    """ vanilla google maps api wrapper """
    return GMAPS.directions(
        origin=origin,
        destination=destination,
        mode=mode
    )
