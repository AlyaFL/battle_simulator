from units import Unit
from soldiers import Soldier
from vehicles import Vehicle
from statistics import geometric_mean
import settings


class Squad:
    """ Squad class 

    Attributes:
        strategy: represents the strategy of the unit 
        random: Random instance for repeatability
    """
    def __init__(self, strategy, random=None):
        self.strategy = strategy
        self.random = random
        self.units = []
        self.create_units()

    @property
    def damage(self):
        """The amount of damage a squad can afflict
        
        Returns:
            int
        """  
        return sum([unit.damage for unit in self.units])

    @property
    def health(self):
        """Squad health value
        
        Returns:
            health (int): sum of units health

        """  
        return sum(unit.health for unit in self.units)

    @property
    def attack_success_probability(self):
        """Squad attack success probability
        
        Returns:
            (int): the geometric average of the attack success probability of each member
        """
        return geometric_mean(u.attack_success_probability for u in self.units)
    
    @property
    def is_alive(self):
        return bool(sum(un.is_alive for un in self.units))   
    
    def get_damage(self, damage):
        """Get damage from enemy

        Methote deals damage to each unit in a unit and checks if health. 
        If the level of health is less than 0, then it removes one from the squad.

        Arg:
            damage: int
        """
        for unit in self.units:
            unit.get_damage(damage)
            if unit.health < 0:
                self.units.remove(unit)

    def get_experience(self):
        for un in self.units:
            un.get_experience()

    def defending(self, units):
        return self.strategies[self.strategy](units)

    def create_units(self):
        """Fills list of units with Soldier or Vehicle instance"""
        for i in range(settings.COUNT_OF_UNITS_PER_SQUAD):
            self.units.append(self.random.choice(
                [Soldier(self.random), Vehicle(self.random)]))