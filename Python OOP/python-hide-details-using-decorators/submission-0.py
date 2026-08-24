class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
    
    # TODO: Add the getter and setter methods
    # Remember to use the @property decorator for the getter methods
    # Remember to use the @setter decorator for the setter methods

    @property
    def health(self) -> int:
        return self.__health
    
    @property
    def power_level(self) -> int:
        return self.__power_level

    @health.setter
    def health(self, nhealth: int):
        if 0 <= nhealth <= 100:
            self.__health = nhealth
        elif nhealth < 0:
            print("You can't set the health to less than 0")
        elif nhealth > 100:
            print("You can't set the health to more than 100")
    
    @power_level.setter
    def power_level(self, npower: int):
        if 1 <= npower <= 10:
            self.__power_level = npower
        elif npower < 1:
            print("You can't set the power level to less than 1")
        elif npower > 10:
            print("You can't set the power level to more than 10")


# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100

print(super_hero.power_level) # this should print 9
super_hero.power_level = 100 # this should print You can't set the power level to more than 10
super_hero.power_level = 0 # this should print You can't set the power level to less than 1


# TODO: print the hero's attributes 

print(f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level")