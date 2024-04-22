class Player:
    def __init__(self,name,form,health,weapon,ammo):
        self.name = name
        self.form = form
        self.health = health
        self.weapon = weapon
        self.ammo = ammo
        self.isAlive = True

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getForm(self):
        return self.form
    def setForm(self,newForm):
        self.form = newForm

    def getHealth(self):
        return self.health
    def setHealth(self,newHealth):
        if newHealth < 0:
            newHealth = 0
        self.health = newHealth

    def getWeapon(self):
        return self.weapon
    def setWeapon(self,newWeapon):
        self.weapon = newWeapon

    def getAmmo(self):
        return self.ammo
    def setAmmo(self,newAmmo):
        self.ammo = newAmmo

    def getIsAlive(self):
        return self.isAlive
    def toggleIsAlive(self):
        if self.isAlive == True:
            self.isAlive = False
        elif self.isAlive == False:
            self.isAlive = True
       
 
class Weapon:
    
    def __init__(self,name,damage,AmmoConsumption):
        self.name = name
        self.damage = damage
        self.ammoConsumption = AmmoConsumption
 

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getDamage(self):
        return self.damage
    def setDamage(self,newDamage):
        self.damage = newDamage

    def getAmmoConsumption(self):
        return self.ammoConsumption
    def setAmmoConsumption(self,newAmmoConsumption):
        self.ammoConsumption = newAmmoConsumption

class Potion:
    def __init__(self, duration):
        self.duration = duration
        
    def getDuration(self):
        return self.duration
    def setDuration(self, newDuration):
        self.duration = newDuration
        
class HealthPotion(Potion):
    def __init__(self,duration,health):
        super().__init__(duration)
        self.health = health
    
    def getHealth(self):
        return self.health
    def setHealth(self, newHealth):
        self.health = newHealth


speler1 = Player("Bob", 0, 100, "roller", 30)
sniper = Weapon("sniper",49.9,1)
potion1 = HealthPotion(60,60)

def hitPlayer(player,weapon):
    if player.getIsAlive():
        newHealth = player.getHealth()- weapon.getDamage()
        player.setHealth(newHealth)
        print("health",speler1.getHealth())

        if player.getHealth()<=0:
            player.toggleIsAlive()
            print("game over")

        newAmmo = player.getAmmo() - weapon.getAmmoConsumption()
        player.setAmmo(newAmmo)
    else:
        print("player is already dead")

def healPlayer(potion, player):
    newHealth = player.getHealth() + potion.getHealth()
    player.setHealth(newHealth)

    potion.setHealth(0)
    print("health:", player.getHealth())    

print(speler1.getName())



print(speler1.getAmmo())
hitPlayer(speler1,sniper)
healPlayer(potion1,speler1)
hitPlayer(speler1,sniper)
healPlayer(potion1,speler1)
hitPlayer(speler1,sniper)
hitPlayer(speler1,sniper)