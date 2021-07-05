from abc import ABCMeta, abstractmethod


class Unit(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self, name, health, recharge):
        self.name = name 
        self.health = health 
        self.recharge = recharge
    
    @property
    def health(self):
        pass

    @property
    def attack(self):
        pass

    @property
    def damage(self):
        pass
