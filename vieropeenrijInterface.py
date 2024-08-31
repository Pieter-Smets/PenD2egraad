import tkinter as tk
class Player:
    def __init__(self, name):
        self.name = name
        self.active = False

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


def on_circle_click(event, circle_id):
    # Change the color of the circle to red when clicked
    canvas.itemconfig(findNextEmpty(circle_id), fill="red")
    

#find the next empty circle in the column
def findNextEmpty(circle_id):
    for id in range(circle_id,43,7):
        if getColor(id) != "white" and id>6:
            return (id-7)
        elif getColor(id) == "white" and id>35:
            return id

#return the color of the specified circle
def getColor(circle_id):
    return canvas.itemcget(circle_id, "fill")

def changePlayer(player1,player2):
    player1.toggleActive()
    player2.toggleActive()

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

player1 = Player("player 1")
player2 = Player("player 2")

player1.toggleActive()
root.mainloop()
