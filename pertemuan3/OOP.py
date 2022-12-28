class Hero:
    name = "alucard"
    hp = 3000
    damage = 200
    defanse = 100

    def __init__( self, name, hp, damage, defanse,):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defanse = defanse
    def attack(self, target):
        target.hp = target.hp - self.damage
        print("sisa hp", target.name, "=", target.hp)

#inisisalisasi class hero

hero1 = Hero("Hayabusa", 2000, 300, 15)
hero2 = Hero("wadimor", 5000, 50, 300)

hero1.attack(hero2)



