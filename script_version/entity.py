from functions import print_and_pause


class Races:
    def __init__(self):
        self.race_bonuses = {
            'Orc': [
                'self.strength += 3',
                'self.cunning -=3'
            ],
            'Elf': [
                'self.strength -=3',
                'self.agility += 2',
                'self.cunning += 1',
            ],
            'Human': [
                'self.strength -= 1',
                'self.agility -= 1',
                'self.cunning += 2',
            ],
        }


class Classes:

    def __init__(self):
        self.class_bonuses = {
            'Warrior': ['self.strength += 2',
                        'self.attack_type = "melee"'
                        ],
            'Archer': ['self.agility += 2',
                       'self.attack_type = "ranged"'
                       ],
            'Rogue': ['self.cunning += 2',
                      'self.attack_type = "melee"'
                      ],
        }

        self.main_attribute = {
            'Warrior': 'strength',
            'Archer': 'agility',
            'Rogue': 'cunning'
        }


class Entity:

    def __init__(self):
        self.entity_class = str
        self.race = str
        self.name = str

        self.attack_type = str

        self.classes = Classes()
        self.races = Races()

        self.current_hp = int
        self.hp = int

        self.min_dmg = int
        self.max_dmg = int

        self.hit_chance = int
        self.crit_chance = int
        self.armor = int
        self.luck = int

        self.level = int
        self.attribute_points = 0

        self.strength = 5
        self.agility = 5
        self.cunning = 5

    @property
    def attributes(self):
        return {'strength': self.strength,
                'agility': self.agility,
                'cunning': self.cunning,
                }

    def set_stats_from_attributes(self):
        self.hp = self.strength * 10
        self.current_hp = self.strength * 10
        self.min_dmg = (self.attributes[self.classes.main_attribute[self.entity_class]] / 4) * 10
        self.max_dmg = (self.attributes[self.classes.main_attribute[self.entity_class]] / 2) * 10
        self.hit_chance = self.attributes['cunning']
        self.crit_chance = self.attributes['agility'] + self.attributes['strength'] / 2
        self.armor = self.attributes['agility']
        self.luck = round(self.attributes['cunning'] / 4)

    def print_advanced_stats(self):
        print_and_pause(f'Strength: {self.attributes["strength"]}, '
                        f'Agility: {self.attributes["agility"]}, '
                        f'Cunning: {self.attributes["cunning"]}, ')
        if self.attribute_points > 0:
            print_and_pause(f'You can still spend {self.attribute_points} attribute points')
        print_and_pause(f'HP: {self.current_hp}/{self.hp}')
        print_and_pause(f'Damage: {self.min_dmg} - {self.max_dmg}')
        print_and_pause(f'Armor: {self.armor}')
        print_and_pause(f'Hit chance: {self.hit_chance} %')
        print_and_pause(f'Crit chance: {self.crit_chance} %')
        print_and_pause(f'Luck chance: {self.luck} %')
