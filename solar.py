#!/usr/bin/env python3
import requests
import datetime

ASTRONOMYAPI_ID="1e403bbb-3853-43de-9ac8-5a58766ed111"
ASTRONOMYAPI_SECRET="95ef34984917b9b7eee61755088c5be048093bfcbcefff3d65f92a8261f951221cbccbc4cc394c3c086fb1fc123c95524ce9654fe3da8fa7fb648a6f874cf12174e649590d7ac48780b0bdb7e5e80752981a6fb6f59cac7fce2235e83d1af010fbd778225313d110b46ea8b1691d83fd"

def get_observer_location(latitude, longitude):
    latitude = str(29.5570295)
    logitude = str(-98.441441)
    # NOTE: Replace with your real return values!
    return None, None

def get_sun_position():
    """Returns the current position of the sun in the sky at the specified location
    Parameters:
    latitude (str)
    longitude (str)
    Returns:
    float: azimuth
    float: altitude
    """
    # NOTE: Replace with your real return values!
    return 0, 0

def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates
    Parameters:
    azimuth (float)
    altitude (float)"""
    print("The Sun is currently at:")

if __name__ == "__main__":
    latitude, longitude = get_location()
    azimuth, altitude = get_sun_position()
    print_position(azimuth, altitude)
