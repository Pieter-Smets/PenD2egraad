#player object with a token and name
class Player:
    def __init__(self,name,token):
        self.name = name
        self.token = token

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getToken(self):
        return self.token
    def setToken(self,NewToken):
        self.token = NewToken

spelbord = [["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]


def printBoard(board):
    for x in board:
        for y in x:
            print(y,"| ",end="")
        print("")

def insertChip(player,columnNumber,spelbord):
    for row in spelbord:
        index = spelbord.index(row)
        if index == len(spelbord)-1:
            row[columnNumber-1] = player.getToken()
        elif row[columnNumber-1] == "O" and spelbord[index+1][columnNumber-1] != "O":
            row[columnNumber-1] = player.getToken()
    

speler1 = Player("speler1","X")
speler2 = Player("speler2","A")

insertChip(speler1,2,spelbord)
insertChip(speler2,2,spelbord)
printBoard(spelbord)
