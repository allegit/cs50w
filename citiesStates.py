'''
    This program demonstrates the concept of dictionary in Python.
'''

# Create a basic mapping of state to abbreivation

states = {
    'North Carolina': 'NC',
    'Massachussetts': 'MA',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY'
}

# Create a basic set of states and home cities in them

cities = {
    'NC': 'Morrisville',
    'MA': 'Boston',
    'CA': 'San Francisco'
}

# Add some cities

cities['NY'] = 'Buffalo'
cities['FL'] = 'Orlando'

# Print put some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("MA state has: ", cities['MA'])

# Print some states
print('-' * 10)
print("California's abbreviation is: ", states['California'])
print("North Carolina's abbreviation is: ", states['North Carolina'])

# Do it by using the same then cities dictionary
print('-' * 10)
print("Florida has: ", cities[states['Florida']])
print("North Carolina has: ", cities[states['North Carolina']])
print("New York has: ", cities[states['New York']])

# Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Print both city and state at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev} and has the city {cities[abbrev]}")

print('-' * 10)
new_state = input("Enter the name of a state to search: ")
# safely get an abbreviation by state that might not be there
state_found = states.get(new_state)

if not state_found:
    print("Sorry no state with name: ", new_state)
else:
    print("State found...")
    print(new_state,"'s abbreviation is:", states[new_state], "and has the city:", cities[states[new_state]])
