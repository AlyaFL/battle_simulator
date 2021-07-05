"""Settings module with the definition of constants"""
import json


with open("config.json") as config:
    settings = json.load(config)

COUNT_OF_ARMIES = settings["count_of_armies"]
COUNT_OF_SQUADS_PER_ARMY = settings["count_of_squads_per_army"]
COUNT_OF_UNITS_PER_SQUAD = settings["count_of_units_per_squad"]

RANDOM_SEED = settings["random_seed"]
