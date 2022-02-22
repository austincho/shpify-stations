stations_map = {}

stations = {
    "Atlantic" : ["Pacific"],
    "Pacific" : ["Atlantic", "Indian", "Sahara", "Gobi"],
    "Indian" : ["Pacific", "Arctic"],
    "Arctic" : ["Indian","Southern"],
    "Southern" : ["Arctic", "Namib", "Bouvet"],
    "Sahara" : ["Pacific"],
    "Gobi" : ["Kalahari", "Pacific"],
    "Kalahari" : ["Gobi", "Mojave"],
    "Mojave" : ["Kalahari", "Namib"],
    "Namib" : ["Mojave", "Southern"],
    "Bouvet" : ["Southern"]
}

def create_stations_map(stations):
    for station_key in stations:
        stations_map[station_key] = calculate_cost_for_station(station_key)

def calculate_cost_for_station(station):
    cost_map = {}
    curr_cost = 1
    visited = []

    queue=[station]
    while queue:
        nextqueue = []
        for station_to_explore in queue:
            visited.append(station_to_explore)
            for connected_station in stations[station_to_explore]:
                if connected_station not in visited:
                    nextqueue.append(connected_station)
                    cost_map[connected_station] = curr_cost
        queue = nextqueue
        curr_cost +=1  

    return cost_map

def calculate_costs(id, origin, destination, balance):
    BASE_FARE = 1
    if origin in stations_map:
        if destination in stations_map[origin]:
            calculated_fare = BASE_FARE + 0.5 * stations_map[origin][destination]
            return (calculated_fare, balance - calculated_fare)
        else:
            raise Exception("Destination does not exist")
    else:
        raise Exception("Origin does not exist")

create_stations_map(stations)
print(stations_map)


print("Stage 1")
print(calculate_costs(1, "Atlantic", "Pacific", 22.50) == (1.5, 21.0))
print(calculate_costs(1, "Atlantic", "Pacific", 1.00) == (1.5, -0.5))
print(calculate_costs(1, "Pacific", "Atlantic", 3.00) == (1.5, 1.5))
print(calculate_costs(1, "Atlantic", "Pacific", 1.50) == (1.5, 0.0))

print("\nStage 2")
print(calculate_costs(3, "Pacific", "Southern", 3.00) == (2.50, 0.50))
print(calculate_costs(1, "Atlantic", "Indian", 50.00) == (2.00, 48.00))
print(calculate_costs(2, "Atlantic", "Southern", 2.00) == (3.00, -1.00))
print(calculate_costs(3, "Southern", "Atlantic", 0.50) == (3.00, -2.50))

print("\nStage 3")
print(calculate_costs(3, "Atlantic", "Namib", 12.00) == (3.50, 8.50))
print(calculate_costs(1, "Kalahari", "Indian", 50.00) == (2.50, 47.50))
print(calculate_costs(2, "Pacific", "Arctic", 2.00) == (2.00, 0.00))
print(calculate_costs(3, "Southern", "Sahara", 0.50) == (3.00, -2.50))

print("\nStage 4")
print(calculate_costs(1, "Sahara", "Bouvet", 12.00) == (3.50, 8.50))
print(calculate_costs(2, "Mojave", "Arctic", 50.00) == (2.50, 47.50))