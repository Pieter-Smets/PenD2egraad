class Player:
    def __init__(self,name,height,health,weapon):
        self.name = name
        self.height = height
        self.health = health
        self.weapon = weapon
        self.isAlive = True

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getHeight(self):
        return self.height
    def setHeight(self,newHeigth):
        self.height = newHeigth

    def getHealth(self):
        return self.health
    def setHealth(self,newHealth):
        if newHealth<0:
            newHealth=0
        self.health = newHealth

    def getWeapon(self):
        return self.weapon
    def setWeapon(self,newWeapon):
        self.weapon = newWeapon

    def getIsAlive(self):
        return self.isAlive
    def setIsAlive(self):
        if self.getIsAlive() == True:
            self.isAlive = False
        elif self.getIsAlive()==False:
            self.getIsAlive = True


class weapon:
    def __init__(self,name,damage,durability):
        self.name = name
        self.damage = damage
        self.durability = durability
        
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getDamage(self):
        return self.damage
    def setDamage(self,newDamage):
        self.damage = newDamage

    def getDurability(self):
        return self.durability
    def setDurability(self,newDurability):
        self.durability = newDurability


speler1 = Player("Bob",180,100,"sword")
sword = weapon("sword",60,100)
print(speler1.getName())

def hitPlayer(player,weapon):
    newHealth = player.getHealth()-weapon.getDamage()
    player.setHealth(newHealth)

    if newHealth <=0:

        player.setIsAlive()
        print("game over")
    print(speler1.getHealth())

    newDurability = weapon.getDurability() - 5
    weapon.setDurability(newDurability)

def healthRegen(player,health):
    newHealth = player.getHealth() + health
    player.setHealth(newHealth)
    print(player.getHealth())

hitPlayer(speler1,sword)
healthRegen(speler1,50)
hitPlayer(speler1,sword)








