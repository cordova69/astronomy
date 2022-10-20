print("Here, we are getting the angle of the sun above the horizon for the -98.441441 degrees longitude and 29.5570295 latitude location at the current time for my address in San Antonio.") 
print()

import astropy.coordinates as coord
from astropy.time import Time
import astropy.units as u


loc = coord.EarthLocation(lon=-98.441441 * u.deg,
lat=29.5570295 * u.deg)
now = Time.now()

altaz = coord.AltAz(location=loc, obstime=now)
sun = coord.get_sun(now)

print(sun.transform_to(altaz).alt)
