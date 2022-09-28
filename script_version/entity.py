from functions import print_and_pause


class Entity:

    def __init__(self):
        self.entity_class = str
        self.race = str
        self.name = str

        self.attack_type = str
        self.current_hp = int

        self.level = int
        self.attribute_points = 0

        self.strength = 5
        self.agility = 5
        self.cunning = 5

        self.main_attribute = str

    @property
    def attributes(self):
        return {'strength': self.strength,
                'agility': self.agility,
                'cunning': self.cunning,
                }

    @property
    def hp(self):
        return self.strength * 10

    @property
    def min_dmg(self):
        return self.attributes[self.main_attribute] / 4 * 10

    @property
    def max_dmg(self):
        return self.attributes[self.main_attribute] / 2 * 10

    @property
    def hit_chance(self):
        return self.cunning

    @property
    def crit_chance(self):
        return self.agility + self.strength / 2

    @property
    def dodge_chance(self):
        return self.agility

    @property
    def armor(self):
        return self.agility + self.strength / 2

    @property
    def luck(self):
        return round(self.cunning / 4)

    def print_advanced_stats(self):
        print_and_pause(f'Strength: {self.strength}, '
                        f'Agility: {self.agility}, '
                        f'Cunning: {self.cunning}, ')
        if self.attribute_points > 0:
            print_and_pause(f'You can still spend {self.attribute_points} attribute points')
        print_and_pause(f'HP: {self.current_hp}/{self.hp}')
        print_and_pause(f'Damage: {self.min_dmg} - {self.max_dmg}')
        print_and_pause(f'Armor: {self.armor}')
        print_and_pause(f'Hit chance: {self.hit_chance} %')
        print_and_pause(f'Crit chance: {self.crit_chance} %')
        print_and_pause(f'Luck chance: {self.luck} %')
