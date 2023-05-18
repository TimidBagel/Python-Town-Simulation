from time import sleep as wait
from math import ceil
from random import *
from person import Person

def run(towns, settings):
    summary = {}
    for town in towns:
        summary[town.name] = {
            "starvation deaths": 0,
            "disease deaths": 0,
            "births": 0,
            "max population": len(town.population),
            "final population": len(town.population),
            "food gathered": 0,
            "food consumed": 0
        }

    for day in range(settings["simulation-length"]):
        for town in towns:
            if len(town.population) <= 0:
                continue;

            # makes 50% of population gather food everyday
            for i in range(ceil(len(town.population) * settings["starvation-rate"] / settings["gather-rate"])):
                if i < len(town.population):
                    town.population[i].task = "gather food"
                    town.population[i].task_timer = 1

            for person in town.population:
                if person.food <= 0:
                    town.population.remove(person)
                    summary[town.name]["starvation deaths"] += 1
                    continue
                
                person.hunger(settings["starvation-rate"])
                person.execute_condition()

                if person.health <= 0:
                    if person.condition == "diseased":
                        town.population.remove(person)
                        summary[town.name]["disease deaths"] += 1
                        continue
                
                if town.storage["food"] > 0:
                    town.storage["food"] -= settings["starvation-rate"]
                    person.food += 1
                    summary[town.name]["food consumed"] += settings["starvation-rate"]

                if person.task != None:
                    if person.execute_task() == "finished":
                        if person.task == "gather food":
                            town.storage["food"] += settings["gather-rate"]
                            summary[town.name]["food gathered"] += settings["gather-rate"]
                            if person.condition != "diseased":
                                disease_chance = randint(1, 50)
                                if disease_chance == 25:
                                    person.condition = "diseased"
                                    person.condition_timer = 10

                if person.sex == "female":
                    if randint(0, settings["birth-chance"]) == settings["birth-chance"]:
                        town.population.append(Person(f"{town.name[:-5]}{len(town.population) + 1}", settings["base-health"], settings["base-food"], [], 10, 0))
                        summary[town.name]["births"] += 1

            if len(town.population) > summary[town.name]["max population"]:
                summary[town.name]["max population"] = len(town.population)

        cont = False
        for town in towns:
            if len(town.population) > 0:
                cont = True

        if cont == False:
            break;
    
    summary["simulation length"] = day + 1

    for town in towns:
        summary[town.name]["final population"] = len(town.population)

    return summary