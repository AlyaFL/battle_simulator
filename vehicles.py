from units import Unit
from soldiers import Soldier
from statistics import geometric_mean
from random import choice


class Vehicle(Unit):
    """ Vehicle class 

    Attributes:
        name: unit type(vehicle)
        health: represents the health of the unit 
        recharge: represents the number of ms required to recharge the unit for an attack
        operators: the number of soldiers required to operate the vehicle

    """

    def __init__(self, random=None):
        self.random = random
        self._health = 100
        self.operators = []
        self.create_operators()

    @property
    def damage(self):  
        """The amount of damage a vehicle can afflict
        
        Returns:
            int
        """  
        return 0.1 + sum(operators.experience for operators in self.operators) / 100

    @property
    def attack_success_probability(self):
        """Vehicles attack success probability
        
        Returns:
            int
        """
        return 0.5 * (1 + self.health / 
        100) * geometric_mean(operator.attack_success_probability 
                for operator in self.operators)

    #def is_alive(self):
     #   return (self.health > 0 and
      #  bool(sum(op.is_alive for op in self.operators)))

    @property
    def health(self):
        """Vehicles health value
        
        Returns:
            health: int
        """
        return (sum(op.health for op in self.operators) /
        len(self.operators) + self._health)

    @health.setter
    def health(self, value):
        self._health = value

    def get_damage(self, damage):
        """Amount of damage vehicles can get from enemy
        
        Args:
            damage: int
        """
        vehicle_damage = damage * 0.6
        operator_damage = damage * 0.2
        other_damage = damage * 0.1
        self.health -= vehicle_damage
        active_operators = [op for op in self.operators]
        random_operators = choice(active_operators)
        other_operators = [op for op in active_operators if op is not random_operators]
        for operator in self.operators:
            operator.get_damage(operator_damage)
            if operator.health < 0:
                self.operators.remove(operator)

    def get_experience(self):
        self.experience += 1

    def create_operators(self):
        """Fills operators[] with Soldier instance"""
        for _ in range(self.random.randint(1, 3)):
            self.operators.append(Soldier(self.random))