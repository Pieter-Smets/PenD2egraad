class Chest:
 
    def __init__(self,weapon,ammo, materials, healing):
        self.isOpen = False
        self.weapon = weapon
        self.ammo = ammo
        self.materials = materials
        self.healing = healing
    
    def getIsOpen(self):
        return self.isOpen 
    
    def setIsOpen(self,newIsOpen):
        self.isOpen = newIsOpen

    def getWeapon(self):
        return self.weapon
    
    def setWeapon(self,newWeapon):
        self.weapon = newWeapon

    def getAmmo(self):
        return self.ammo
    
    def setAmmo(self,newAmmo):
        self.ammo = newAmmo

    def getMaterials(self):
        return self.materials
    
    def setMaterials(self,newMaterials):
        self.materials = newMaterials

    def getHealing(self):
        return self.healing
    
    def setHealing(self, newHealing):
        self.healing = newHealing

class Player:
    def __init__(self,name,health,weapon,ammo,materials):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.ammo = ammo
        self.materials = materials
        
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getWeapon(self):
        return self.weapon
    def setWeapon(self,newWeapon):
        self.weapon = newWeapon

    def getAmmo(self):
        return self.ammo
    def setAmmo(self,newAmmo):
        self.ammo = newAmmo

    def getMaterials(self):
        return self.materials
    def setMaterials(self,newMaterials):
        self.materials = newMaterials

    def getHealth(self):
        return self.health
    def setHealth(self, newHealth):
        self.health = newHealth


firstChest = Chest("sniper",6,"metal",50)
player1 = Player("playerOne",100,"pistol",10,None)

print(firstChest.getHealing())
#firstChest.setHealing(0)
#print(firstChest.getHealing())

def openChest(chest,player):
    weapon = chest.getWeapon()
    player.setWeapon(weapon)
    chest.setWeapon("")

    newAmmo = player.getAmmo()+chest.getAmmo()
    player.setAmmo(newAmmo)
    chest.setAmmo(0)

    newMaterial = chest.getMaterials()
    player.setMaterials(newMaterial)
    chest.setMaterials("")

    newHealth = player.getHealth() + chest.getHealing()
    player.setHealth(newHealth)
    chest.setHealing(0)

openChest(firstChest,player1)
print("breakpoint")
