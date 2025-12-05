'''

Imagine writing a game called Orcs Vs. Goblins. You will, of course,
need goblins:

>>> goby = Goblin('Goby')
>>> goby.name
'Goby'

>>> goby.hitpoints
10
>>> goby.damage
3

You'll also need orcs, who are a bit bigger and tougher:

>>> morgash = Orc('Morgash')
>>> morgash.name
'Morgash'
>>> morgash.hitpoints
15
>>> morgash.damage
5

You can check whether a creature is alive:

>>> morgash.is_alive()
True
>>> morgash.hitpoints = 0
>>> morgash.is_alive()
False
>>> morgash.hitpoints = 10
>>> morgash.is_alive()
True

Both goblins and orcs inherit from a class called Critter.
IMPORTANT: Put as many methods and member variables as possible in
this base class. Can you find a way to put ALL the methods in Critter?

>>> isinstance(goby, Critter)
True
>>> isinstance(morgash, Critter)
True

This being a fighting game, critters can (and will) attack each other.
(Notice the attack() method returns the amount of damage done.)

>>> goby.hitpoints
10
>>> morgash.hitpoints
10
>>> morgash.attack(goby)
5
>>> goby.hitpoints
5
>>> goby.attack(morgash)
3
>>> goby.attack(morgash)
3
>>> morgash.hitpoints
4

Hit points can't go below zero, though:
>>> goby.attack(morgash)
3
>>> morgash.hitpoints
1
>>> goby.attack(morgash)
1
>>> morgash.hitpoints
0
>>> goby.attack(morgash)
0
>>> morgash.hitpoints
0

'''

# Write your code here:
class Critter:
    def __init__(self, name) -> None:
        self._name = name;
        self._damage = 3;
        self._hitpoints = 10;
    
    @property
    def name(self):
        return self._name;
    
    @property
    def hitpoints(self):
        return max(self._hitpoints, 0);
    
    @hitpoints.setter
    def hitpoints(self, value):
        self._hitpoints = value;
    
    @property
    def damage(self):
        return self._damage;
    
    def attack(self, enemy):
        hitpoints_before_attack = enemy.hitpoints;

        enemy._hitpoints = enemy._hitpoints - min(self.damage, enemy.hitpoints)
        return min(hitpoints_before_attack, self.damage);
    
    def is_alive(self):
        return self.hitpoints > 0;

class Goblin(Critter):
    def __init__(self, name) -> None:
        super().__init__(name)

class Orc(Critter):
    def __init__(self, name) -> None:
        super().__init__(name);
        self._damage = 5;
        self._hitpoints = 15;

goby = Goblin("Goby");
morgash = Orc("Morgash");

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# From Powerful Python. Copyright MigrateUp LLC. All rights reserved.
