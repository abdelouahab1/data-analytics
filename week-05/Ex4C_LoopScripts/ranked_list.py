cities = ['Madrid', 'Tokyo', 'New york', 'Paris', 'London']

for index, cities in enumerate(cities):
    if index == 0:
        print(f'{index + 1}, {cities} <- top pick!')
    else:
        print(index + 1, cities)