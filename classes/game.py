import random

class bcolors:
    HEADER = '\033[95m'
    Okblue = '\033[94m'
    OkGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[4m'
    BOLD = '\033[0m'
    UNDERLINE = '\033[1m'


class Person:
    def __init__(self,hp,mp,atk,df,magic,items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack','Magic','Items']
        pass

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
    def generate_spell_damage(self,i):
        mgl = self.magic[i]['damage'] - 5
        mgh = self.magic[i]['damage'] + 5
        return random.randrange(mgl,mgh)
    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp <0:
            self.hp = 0
            return self.hp
    def get_hp(self):
            return self.hp
    def get_max_hp(self):
            return self.maxhp
    def get_mp(self):
         return self.mp
    def get_max_mp(self):
         return self.maxmp
    def reduce_mp(self,cost):
         self.mp-= cost
         