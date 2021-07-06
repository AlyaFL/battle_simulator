from random import Random, choice
import strategy
import settings
from army import Army
from logger import Logger


class Main:
    strategies =[strategy.StongestEnemy,
                strategy.RandomEnemy,
                strategy.WeakestEnemy]

    def __init__(self, random_s):
        self.random = Random(random_s)
        self.armies = []
        self.create_armies()
        self.logger = Logger()

    def create_armies(self):
        """Army list instance"""
        for i in range(settings.COUNT_OF_ARMIES):
            strategy = self.random.choice(Main.strategies)
            self.armies.append(Army(f"Army {i+1}", strategy, self.random))

    def check_alive(self):
        """Check army for the alive squads in it
        
        If armies has no squads than it is removed
        """
        self.armies = [army for army in self.armies if army.squads]

    def run(self):
        while len(self.armies) > 1:
            for ar in self.armies:
                if ar.health <= 0:
                    break
                enemy_armies = [enemies for enemies in self.armies if enemies is not ar]
                enemy_army = ar.strategy.select(enemy_armies)
                if ar.attack_success_probability > enemy_army.attack_success_probability:
                    self.logger.write(f"{ar.name} attacks {enemy_army.name}")
                    ar.attack(enemy_army)
                    self.check_alive()
                    for ar in self.armies:
                        self.logger.write(f"{ar.name} - {ar.health} health")
        self.logger.close()

RANDOM_SEED = settings.RANDOM_SEED
if __name__ == "__main__":
    game = Main(RANDOM_SEED)
    game.run()