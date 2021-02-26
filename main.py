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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(new_country, new_visit,new_city):
    new_log = {}
    new_log["country"] = new_country
    new_log["visits"] = new_visit
    new_log["cities"] = new_city
    travel_log.append(new_log)

#🚨 Do not change the code below
add_new_country(new_country = "Russia", new_visit = 2, new_city = ["Moscow", "Saint Petersburg"])
print(travel_log)



