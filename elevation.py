import requests
import urllib
import pandas as pd

# USGS Elevation Point Query Service
url = r'https://nationalmap.gov/epqs/pqs.php?'

# coordinates with known elevation 
lat = [29.5570295]
lon = [-98.441441]

# create data frame
df = pd.DataFrame({
    'lat': lat,
    'lon': lon
})

def elevation_function(df, lat_column, lon_column):
    """Query service using lat, lon. add the elevation values as a new column."""
    elevations = []
    for lat, lon in zip(df[lat_column], df[lon_column]):

        # define rest query params
        params = {
            'output': 'json',
            'x': lon,
            'y': lat,
            'units': 'Meters'
        }

        # format query string and return query value
        result = requests.get((url + urllib.parse.urlencode(params)))
        elevations.append(result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation'])

    df['elev_meters'] = elevations

elevation_function(df, 'lat', 'lon')
df.head()

print()
print("This is printing latitude, longitude and elevation in meters for my location in San Antonio.")
print()

print(df.head())

