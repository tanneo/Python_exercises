#dictionary is like a list but instead of only using numbers to store data, you can use anything
#This lets you treat a dictionary like it is a database for storing and organising data
#A dictionary always associates one thing with another, no matter what it is

#create a mapping of state to abbreviaion of states
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MY'
}

#create a basic set of states and some cities in them cities
cities = {
    'CA': 'San Fransisco',
    'MY': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print('OR state has:', cities['OR'])

#print some states
print('-' * 10)
print('Michigans abbreviation is: ', states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city: {city}")

#now co both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#get an abbreviation of a state that might not be there
print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no texas")

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

aus_states = {
    'Queensand': 'QLD',
    'New South Wales': 'NSW',
    'Tasmania': 'TAS',
    'Western Australia': 'WA',
    }

#create a basic set of states and some cities within those cities
aus_cities = {
    'QLD' : 'Brisbane',
    'NSW' : 'Sydney',
    'WA' : 'Perth'
}

#add some more cities
aus_cities['TAS'] = "Hobart"
aus_cities['QLD'] = 'Cairns'

#print out some cities
print(f"QLD has :", aus_cities['QLD'])

#print out some states
print(f"New South Wales abbreviation is:", aus_states['New South Wales'])

#print every state abbreviation
for aus_state, abbrev in list(aus_states.items()):
    print(f"{aus_state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(aus_cities.items()):
    print(f"{abbrev} has the city: {city}")

#now co both at the same time
print('-' * 10)
for state, abbrev in list(aus_states.items()):
    print(f"{aus_state} state is abbreviated {abbrev}")
    print(f"and has city {aus_cities[abbrev]}")

