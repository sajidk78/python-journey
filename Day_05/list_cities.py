# List of 3 cities

cities= []

for i in range(3):
    city = input(f"\n Enter city {i+1} : ")



    if city == "":
        print("\n City can not be emputy")
        continue
    city=city.strip().title()
    cities.append(city)

print("\n ==== CITIES ====")

for city in cities:
    print(f"\n City {city}")
print(f"\n Total Cities {len(cities)}")
