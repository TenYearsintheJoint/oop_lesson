import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load cities data
cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Load countries data
countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps) / len(temps))
print()

# Print all cities in Italy
my_country = 'Italy'
italy_cities = [city['city'] for city in cities if city['country'] == my_country]
print("All the cities in", my_country, ":")
print(italy_cities)
print()

# Print the average temperature for all cities in Italy
italy_temps = [float(city['temperature']) for city in cities if city['country'] == my_country]
print("The average temperature of all the cities in Italy:")
print(sum(italy_temps) / len(italy_temps))
print()

# Print the max temperature for all the cities in Italy
print("The max temperature of all the cities in Italy:")
print(max(italy_temps))
print()

# Filter function to select items based on a condition
def filter(condition, dict_list):
    return [item for item in dict_list if condition(item)]

# Aggregate function to apply an aggregation function on a specific key
def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [float(item[aggregation_key]) for item in dict_list]
    return aggregation_function(values)

# Use filter and aggregate functions to:
# - print the average temperature for all cities in Italy
# - print the average temperature for all cities in Sweden
# - print the min temperature for all cities in Italy
# - print the max temperature for all cities in Sweden

# Average temperature for Italy
italy_cities = filter(lambda x: x['country'] == 'Italy', cities)
italy_avg_temp = aggregate('temperature', lambda temps: sum(temps) / len(temps), italy_cities)
print("Average temperature in Italy:", italy_avg_temp)

# Average temperature for Sweden
sweden_cities = filter(lambda x: x['country'] == 'Sweden', cities)
sweden_avg_temp = aggregate('temperature', lambda temps: sum(temps) / len(temps), sweden_cities)
print("Average temperature in Sweden:", sweden_avg_temp)

# Minimum temperature in Italy
italy_min_temp = aggregate('temperature', min, italy_cities)
print("Min temperature in Italy:", italy_min_temp)

# Maximum temperature in Sweden
sweden_max_temp = aggregate('temperature', max, sweden_cities)
print("Max temperature in Sweden:", sweden_max_temp)
