from town import *
from building import *
from person import *

import day_manager

data = {}
output = ""

settings = {
    "simulation-length": 500,
    "simulation-count": 10,
    "base-health": 20,
    "base-food": 30,
    "starvation-rate": 1,
    "gather-rate": 2,
    "base-population": 20,
    "birth-chance": 270
}

towns = []

fredville = Town("Fredville", [], 0, [])
tedville = Town("Tedville", [], 0, [])
drewville = Town("Drewville", [], 0, [])
towns.append(fredville)
towns.append(tedville)
towns.append(drewville)

for i in range(settings["simulation-count"]):
    for town in towns:
        town.population = []
    
    for town in towns:
        for j in range(settings["base-population"]):
            town.population.append(Person(f"{town.name[:-5]}{j}", settings["base-health"], settings["base-food"], [], 10, 10))

    summary = day_manager.run(towns, settings)
    data[f"SIMULATION {i}"] = summary

average_disease_deaths = 0
average_starvation_deaths = 0
average_births = 0
average_final_population = 0
average_max_population = 0

for sim in data:
    output += sim
    output += f"\n\nSimulation length: {data[sim]['simulation length']}"

    for item in data[sim]:
        if "ville" in item:
            average_final_population += data[sim][item]["final population"]
            average_max_population += data[sim][item]["max population"]

            output += f"\n\n{item}:"

            for set in data[sim][item]:
                output += f"\n{set} : {data[sim][item][set]}"
            
            average_disease_deaths += data[sim][item]["disease deaths"]
            average_starvation_deaths += data[sim][item]["starvation deaths"]

    output += "\n\n"

iterations = len(towns) * len(data)

output += "Simulation results:\n\n"

output += "\nAverage starvation deaths : " + str(int(average_starvation_deaths / iterations))
output += "\nAverage disease deaths : " + str(int(average_disease_deaths / iterations))
output += "\nAverage births : " + str(int(average_births / iterations))
output += "\nAverage final population : " + str(int(average_final_population / iterations))
output += "\nAverage maximum population : " + str(int(average_max_population / iterations))

print(output)

input() # EOF pause