travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(new_country, new_visit, new_city):
    new_location = {}
    new_location["country"] = new_country
    new_location["visits"] = new_visit
    new_location["cities"] = new_city
    travel_log.append(new_location)


add_new_country(new_country = "Russia", new_visit = 2, new_city = ["Moscow", "Saint Petersburg"])
print(travel_log)



