from operator import attrgetter
from random import choice, Random
import settings


class RandomEnemy:
    @staticmethod
    def select(enemies):
        return choice(enemies.units)
        
class StongestEnemy:
    @staticmethod
    def select(enemies):
        return sorted(enemies, key=lambda enemy: enemy.health, reverse=True)[0]
    
class WeakestEnemy:
    @staticmethod
    def select(enemies):
        return sorted(enemies, key=lambda enemy: enemy.health)[0]
