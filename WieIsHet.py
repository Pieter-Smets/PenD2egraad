class Personage:

    def __init__(self, naam, hoofddeksel, geslacht, bril, haarkleur):
        # Constructor method to initialize the attributes of the Personage class.
        self.hoofddeksel = hoofddeksel  # Attribute for the headgear of the personage.
        self.geslacht = geslacht  # Attribute for the gender of the personage.
        self.bril = bril  # Attribute for whether the personage wears glasses.
        self.haarkleur = haarkleur  # Attribute for the hair color of the personage.
        self.naam = naam
    
    def getNaam(self):
        return self.naam
    
    def setNaam(self, newNaam):
        self.naam = newNaam

    def getHoofddeksel(self):
        # Getter method to retrieve the headgear attribute.
        return self.hoofddeksel

    def setHoofddeksel(self, newHoofddeksel):
        # Setter method to update the headgear attribute.
        self.hoofddeksel = newHoofddeksel

    def getGeslacht(self):
        # Getter method to retrieve the gender attribute.
        return self.geslacht

    def setGeslacht(self, newGeslacht):
        # Setter method to update the gender attribute.
        self.geslacht = newGeslacht

    def getBril(self):
        # Getter method to retrieve the glasses attribute.
        return self.bril

    def setBril(self, newBril):
        # Setter method to update the glasses attribute.
        self.bril = newBril

    def getHaarkleur(self):
        # Getter method to retrieve the hair color attribute.
        return self.haarkleur

    def setHaarkleur(self, newHaarkleur):
        # Setter method to update the hair color attribute.
        self.haarkleur = newHaarkleur

class Speler:
    def __init__(self, naam, gekozenPersonage):
        # Constructor method to initialize the attributes of the Speler class.
        self.isZijnBeurt = False  # Attribute to track whether it is the player's turn.
        self.naam = naam  # Attribute for the name of the player.
        self.gekozenPersonage = gekozenPersonage  # Attribute for the chosen character of the player.
        self.overgeblevenPersonages = []  # List attribute to store remaining characters for the player.

    def getIsZijnBeurt(self):
        # Getter method to retrieve the isZijnBeurt attribute.
        return self.isZijnBeurt

    def setIszijnBeurt(self, newIsZijnBeurt):
        # Setter method to update the isZijnBeurt attribute.
        self.isZijnBeurt = newIsZijnBeurt

    def getNaam(self):
        # Getter method to retrieve the name attribute.
        return self.naam

    def setNaam(self, newNaam):
        # Setter method to update the name attribute.
        self.naam = newNaam

    def getGekozenPersonage(self):
        # Getter method to retrieve the gekozenPersonage attribute.
        return self.gekozenPersonage

    def setGekozenPersonage(self, newGekozenPersonage):
        # Setter method to update the gekozenPersonage attribute.
        self.gekozenPersonage = newGekozenPersonage

    def getOvergeblevenPersonages(self):
        # Getter method to retrieve the overgeblevenPersonages attribute.
        return self.overgeblevenPersonages

    def setOvergeblevenPersonages(self, personageOmTeVerwijderen):
        # Setter method to remove a character from the overgeblevenPersonages list.
        self.overgeblevenPersonages.remove(personageOmTeVerwijderen)

lst_personages = []

def giveCharacterByName(naam):
    for pers in lst_personages:
        if pers.getNaam() == naam:
            return pers

def runGame():
    isGewonnen = False

    naam = input("geef je naam in: ")
    naamGekozenPersonage = input("geef de naam in van jouw gekozen personage")
    gekozenPersonage = giveCharacterByName(naamGekozenPersonage)
    speler1 = Speler(naam,gekozenPersonage)

    naam = input("geef je naam in: ")
    naamGekozenPersonage = input("geef de naam in van jouw gekozen personage")
    gekozenPersonage = giveCharacterByName(naamGekozenPersonage)
    speler2 = Speler(naam,gekozenPersonage)


    while not(isGewonnen):
        print("spel wordt gespeeld")