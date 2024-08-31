import tkinter as tk
class Player:
    def __init__(self, name, color,active):
        self.name = name
        self.active = False
        self.color = color
        self.active = active

    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
    
    def isActive(self):
        return self.active
    def toggleActive(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def getColor(self):
        return self.color
    def setColor(self, newColor):
        self.color = newColor


def on_circle_click(event, circle_id):
    # Change the color of the circle to red when clicked
    canvas.itemconfig(findNextEmpty(circle_id), fill=getPlayerColor())
    
def getPlayerColor():
    if player1.isActive():
        return player1.getColor()
    elif player2.isActive():
        return player2.getColor()

#find the next empty circle in the column
def findNextEmpty(circle_id):
    pass

#return the color of the specified circle
def getColor(circle_id):
    return canvas.itemcget(circle_id, "fill")

def changePlayer(player1,player2):
    player2.toggleActive()
    player1.toggleActive()

def checkVertical(circle_id):
    pass

def checkHorizontal(circle_id):
    pass

def checkLeftDiagonal(circle_id):
    pass

def checkRightDiagonal(circle_id):
    pass

root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=600)
canvas.pack()

circle_radius = 50
circle_distance = 100
offset_x = circle_distance // 2 #50
offset_y = circle_distance // 2 #50

# Store the circle IDs in a list
circle_ids_rows = []

#place the circles on the canvas
for row in range(6):
    circle_ids_rows.append([])
    for col in range(7):
        x1 = col * circle_distance +2 #+ offset_x - circle_radius #100+50-50
        y1 = row * circle_distance +2#+ offset_y - circle_radius #100+50-50
        x2 = col * circle_distance + offset_x + circle_radius +2#100+50+50
        y2 = row * circle_distance + offset_y + circle_radius +2#100+50+50
        circle = canvas.create_oval(x1, y1, x2, y2, fill="white", outline="black")
        circle_ids_rows[row].append(circle)
        
        # Bind the click event to the circle
        canvas.tag_bind(circle, '<Button-1>', lambda event, id=circle: on_circle_click(event, id))

player1 = Player("player 1","red",True)
player2 = Player("player 2","blue",False)

player1.toggleActive()
root.mainloop()

