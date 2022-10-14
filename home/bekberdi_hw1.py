class Hero:
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        self.hp += 100

    def two_damage(self):
        self.damage *= 2

    def greetings(self):
        return f"my name is {self.name}"

    def brand_phrase(self):
        return "good will win"

#
# tom = Hero(name='Tom', nickname='alucard', hp=100, damage=50)
# print(tom.name, tom.nickname, tom.hp, tom.damage)
# tom.heal()
#
# bob = Hero(name='Bob', nickname='gremmy', hp=30, damage=150)
# print(bob.name, bob.nickname, bob.hp, bob.damage)
# bob.two_damage()
#
# raven = Hero(name='Raven', nickname='lu', hp=50, damage=50)
# print(raven.name, raven.nickname, raven.hp, raven.damage)
# raven.greetings()
#
# bazz = Hero(name='Bazz', nickname='The Heat', hp=200, damage=100)
# print(bazz.name, bazz.nickname, bazz.hp, bazz.damage)
# bazz.brand_phrase()
