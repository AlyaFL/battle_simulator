from squads import Squad
from statistics import geometric_mean
import settings


class Army:
    """Army class 

    Contains a group of units (squad)

    Attributes:
        name: army name
        strategy: strategy name
        squad: list of squad
    """
    def __init__(self, name, strategy, random=None):
        self.name = name
        self.strategy = strategy
        self.squads = []
        self.random = random
        self.create_squads()
        

    @property
    def health(self):
        """Army health value
        
        Returns:
            health(int): sum of health of all squad in army
        """
        return sum(sq.health for sq in self.squads)

    @property
    def damage(self):
        """Army damage value
        
        Returns:
            (int): sum of damage value of all squad in army
        """ 
        return sum(sq.damage for sq in self.squads)

    @property
    def attack_success_probability(self):
        """Army attack success probability
        
        Returns:
            (int): average of the attack success probability of army squad
        """
        return geometric_mean(sq.attack_success_probability for sq in self.squads)

    def attack(self, enemy):
        enemy.get_damage(self.damage)
        for sq in self.squads:
            squad.get_experience()

    def get_damage(self, damage):
        """Amount of damage army can get from enemy
        
        Args:
            damage: int
        """
        for sq in self.squads:
            sq.get_damage(damage)
            if sq.health <= 0:
                self.squad.remove(sq)

    def create_squads(self):
        for i in range(settings.COUNT_OF_SQUADS_PER_ARMY):
            self.squads.append(Squad(self.strategy, self.random))