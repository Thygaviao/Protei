import requests

coordinates = '60.05718775,30.27751005081418'
address = '7 к3, набережная реки Каменки, округ Коломяги,'\
          ' Санкт-Петербург, Северо-Западный федеральный округ, 197375, Россия'
payloadAddress = {'q': address, 'format': 'json'}
payloadCoordinates = {'q': coordinates, 'format': 'json'}

searchByAddress = requests.get("https://nominatim.openstreetmap.org/search.php", params=payloadAddress)
searchByCoordinates = requests.get("https://nominatim.openstreetmap.org/search.php", params=payloadAddress)
for i in searchByAddress.json():
    lat = str(i.get('lat'))
    lon = str(i.get('lon'))
    if lat + ',' + lon == coordinates:
        print("Finding coordinates by address works correctly!")

for i in searchByCoordinates.json():
    display_name = str(i.get('display_name'))
    if display_name == address:
        print("Finding address by coordinates works correctly!")
