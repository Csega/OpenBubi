import urllib.parse  # for parsing urls
import os  # for running termux-location
import json  # for converting the command-line output to dictionary
import openbubi
import sys  # for path manipulation
sys.path.append("../")  # add openbubi.py's folder to the current path

"""
The purpose of this example code is to locate the nearest BuBi station for you
based on your phone's termux location data (command line for Android).
"""

Budapest = openbubi.BubiMap()

# read the current location
currentLocation = os.popen("termux-location").read()

currentLocationDict = json.loads(currentLocation)  # convert it to a dictionary

lat = currentLocationDict["latitude"]
lon = currentLocationDict["longitude"]  # parse it

# call getNearestStation(), and provide lat, lon
nearestStation = Budapest.getNearestStation(lat, lon)
# this will return the nearest station's name

nearestStationInfo = {
    "name": nearestStation,
    # count the bikes on that station
    "bikesOnStation": Budapest.countBikesOnStation(nearestStation),
    # get the coordinates of that station, and convert it to a dictionary
    "coordinates": json.loads(Budapest.getCoordinatesOfStation(nearestStation))
}

startingPoint = urllib.parse.quote(f"{lat},{lon}")
# make a starting point in a url-friendly format (based on the current coordinates)
destinationPoint = urllib.parse.quote(
    f"{nearestStationInfo['coordinates']['lat']},{nearestStationInfo['coordinates']['lon']}")
# make an ending point in a url-friendly format (based on the station's coordinates)
googlemapsurl = f"https://www.google.com/maps?f=d&saddr={startingPoint}&daddr={destinationPoint}&dirflg=d"
# generate the Google Maps URL

# ^
# |
# calculate a Google Maps route to the station

print(
    f"""
 Station found...

 Informations:

 - Station name: {nearestStationInfo["name"]}
 - Bikes on station: {nearestStationInfo["bikesOnStation"]}
 - Coordinates of station: {nearestStationInfo["coordinates"]}
 - Google Maps route to the station: {googlemapsurl}
 """
)
# printing out
