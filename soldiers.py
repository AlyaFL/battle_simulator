from units import Unit
from random import randint


class Soldier(Unit):
    """ Soldier class 

    Attributes:
        name: unit type(soldier)
        health: represents the health of the unit 
        recharge: represents the number of ms required to recharge the unit for an attack
        experience: represents the soldier experience

    """

    def __init__(self, random):
        self.random = random
        self._experience = 1
        self._health = 50
    
    @property
    def experience(self):
        """Soldier experience value
        
        Returns:
            experience: int
        """
        return self._experience

    @experience.setter
    def experience(self, value):
        if 0 < self.experience < 50:
            self._experience = value

    @property
    def health(self):
        """Soldier health value
        
        Returns:
            health: int
        """        
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def attack_success_probability(self):
        """Soldiers attack success probability
        
        Returns:
            int
        """
        return 0.5 * (1 + self.health/100) * randint(50 + self.experience, 100) / 100

    @property
    def damage(self):  
        """The amount of damage a soldier can afflict
        
        Returns:
            int
        """  
        return 0.05 + self.experience / 100

    @property
    def get_damage(self, damage):
        """Amount of damage soldier can get from enemy"""
        if self.health != 0: 
            self.health -= damage

    @property
    def is_alive(self):
        """Сhecks the health of a soldier"""
        return self.health > 0

    def get_experience(self):
        self.experience += 1
