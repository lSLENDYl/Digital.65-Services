from geopy.geocoders import Nominatim

def getLocbycord(latitude, longtitude):
    geoLoc = Nominatim(user_agent="GetLoc")
    strin = str(latitude) + ", " + str(longtitude)
    locname = geoLoc.reverse(strin)
    return locname.address

def getLocbypos(position):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(position)
    print(getLoc.address)
    return (getLoc.latitude, getLoc.longitude)

lat = input()
lon = input()
pos = input()

if len(pos) == 0 and (len(lat == 0) and len(lon == 0)):
    print("ErrorLocation")
elif len(pos) != 0 and (len(lat != 0) and len(lon != 0)):
    print(getLocbypos(pos))
elif len(pos) == 0 and (len(lat != 0) and len(lon != 0)):
    print(getLocbycord(lat, lon))
elif len(pos) != 0 and (len(lat == 0) and len(lon == 0)):
    print(getLocbypos(pos))