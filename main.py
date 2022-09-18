import webbrowser
import PIL.Image
import PIL.ExifTags
from gmplot import gmplot
from geopy.geocoders import Nominatim
import webbrowser

img = PIL.Image.open("8.jpg")#your image path goes here
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}
#print(exif['GPSInfo']) #Dictonary form north and east values
north = exif['GPSInfo'][2]
east = exif['GPSInfo'][4]

print("NORTH: ",north)
print("EAST: ",east)

lat = ((((north[0] * 60) + north[1]) * 60) + north[2]) / 60 / 60
lon = ((((east[0] * 60) + east[1]) * 60) + east[2]) / 60 / 60

lat, lon = float(lat), float(lon)

print("LATITUDE: ",lat)
print("LONGITUDE: ",lon)


gmap = gmplot.GoogleMapPlotter(lat, lon, 12) #12 is zoom
gmap.marker(lat, lon, "cornflowerblue")
gmap.draw("location.html")

webbrowser.open("location.html", new=2)

geoloc = Nominatim(user_agent="GetLoc")
locname = geoloc.reverse(f"{lat}, {lon}")

print("ADDRESS: ",locname.address)