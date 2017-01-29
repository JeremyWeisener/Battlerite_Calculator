class Skill:
    def __init__(self, name, btn, desc, energy, cooldown, img):
        self.name = name
        self.btn = btn
        self.dmg = 0
        self.heal = 0
        self.desc = desc
        self.iframes = False
        self.type = "None"
        self.ex = False
        self.energy = energy
        self.img = img
        self.casttime = 0
        self.energygained = 0
        self.counter = False
        self.cooldown = cooldown
        self.movement = False
        self.is_moving = False


class Champion:

    def __init__(self, name):

        self.name = name
        self.hp = 0
        self.desc = ""
        self.img = ""

    def addSkill(self, sname, btn, desc, energy, cooldown, img):
        self.sname = Skill(sname, btn, desc, energy, cooldown, img)

#note