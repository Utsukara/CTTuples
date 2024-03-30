
# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: 
# (traveler_name, origin, destination)


# The function should format and return a string that lists each itinerary. 
# For example, if the input is :

flight_itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

# the output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def print_itinerary(flight_list):
    for index, itinerary_info in enumerate(flight_list):
        print(f"Itinerary {index + 1}: {itinerary_info[0]} - From {itinerary_info[1]} to {itinerary_info[2]}")

print_itinerary(flight_itinerary)