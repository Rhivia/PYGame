class new:
    def __init__(self, name):
        self.name = name
        self.hungerMax = 50
        self.hunger = self.hungerMax
        self.HPMax = 50
        self.HP = self.HPMax
        self.age = 0

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setHunger(self, value):
        if((self.hunger + value) > self.hungerMax):
            self.hunger = self.hungerMax
        else:
            self.hunger += value
    def getHunger(self):
        return self.hunger

    def setHP(self, value):
        if ((self.HP + value) > self.HPMax):
            self.HP = self.HPMax
        else:
            self.HP += value
    def getHP(self):
        return self.HP

    def setAge(self, value):
        self.age += value
    def getAge(self):
        return self.age

    def getHumor(self):
        return ((self.hunger + self.HP) / 2)