import geoip2.database

def get_location(ip_address):
    reader = geoip2.database.Reader('path/to/GeoIP2-City.mmdb')
    response = reader.city(ip_address)
    # Extract the relevant information from the response
    country = response.country.name
    city = response.city.name
    latitude = response.location.latitude
    longitude = response.location.longitude
    return country, city, latitude, longitude
ip_address = "123.456.789.0"  # Replace with the desired IP address
country, city, latitude, longitude = get_location(ip_address)
print(f"IP: {ip_address}")
print(f"Country: {country}")
print(f"City: {city}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
