'''
Turtle Interface - First Attempt
'''
 
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import turtlefigure
import turtle 
 
#--------------------- make the fram and turtle objects ------    
 
# make the root frame and give its geometry
root = Tk()
root.title( "Turtle Figures Generator")
root.geometry("800x500+300+50")
root.configure(bg = "#B8D3F2")
 
# ---------------  functions to control the interface ---------
 
def onClearF():
     # define how clear events are handled
     orderStr.set("")
     lengthStr.set("")
 
     # clear the screen
     canvas.delete("all")
     pen = turtle.RawTurtle(canvas)
     pen.color("#355d86")
     pen.speed(0)
     pen.width(3)
     information.configure(text = "Figure has been cleared. Please try to draw another one.")
 
# end clearF

def onDrawF():

     # reset canvas and pen
     canvas.delete("all")
     pen = turtle.RawTurtle(canvas)
     pen.color("#355d86")
     pen.speed(0)
     pen.width(3)
     # get the oder string converted to int
     order = int(orderStr.get())
 
     # convert length to float
     length = float(lengthStr.get())
 
     # find the selected figure from the combobox
     turtleIndex = figureList.index(figureStr.get()) 

     if turtleIndex == 0:
         # draw binary tree
         pen.up();pen.setx(-300);pen.down()
         turtlefigure.tree(order, length, pen)
        
         information.configure( text = "This is a Binary Tree with order "
                               + str(order)+ " and length " + str(length) + ". ")
         
         
     elif turtleIndex == 1:
         # draw quad tree    
         pen.up(); pen.setx(-200); pen.down()
         turtlefigure.tree4(order, length, pen)
         information.configure( text = "This is a Quad Tree with order "
                               + str(order)+ " and length " + str(length) + ". ")

     elif turtleIndex == 2:
          #draw fern
          pen.up();pen.setx(-200);pen.down()
          turtlefigure.fern(order, length, pen)
          information.configure( text = "This is a Fern Tree with order "
                               + str(order)+ " and length " + str(length) + ". ")

     elif turtleIndex == 3:
          #draw serpinsky gasket
          pen.up();pen.setx(-200); pen.sety(-length/2); pen.down()
          turtlefigure.s(order, length, pen)
          information.configure( text = "This is a Serpinsky Gasket with order "
                               + str(order)+ " and length " + str(length) + ". ")

     elif turtleIndex == 4:
          #draw koch
          pen.up();pen.setx(-200);pen.down()
          turtlefigure.koch(order, length, pen)
          information.configure( text = "This is a Koch Curve with order "
                               + str(order)+ " and length " + str(length) + ". ")

     elif turtleIndex == 5:
          #draw Snowflake
          pen.up();pen.setx(-200); pen.sety(100); pen.down()
          turtlefigure.snowFlake(order, length, pen)
          information.configure( text = "This is a Snowflake with order "
                               + str(order)+ " and length " + str(length) + ". ")
     elif turtleIndex == 6:
          #draw antiSnowflake
          pen.up();pen.setx(-200); pen.sety(-100); pen.down()
          turtlefigure.antiSnowFlake(order, length, pen)
          information.configure( text = "This is an Anti-Snowflake with order "
                               + str(order)+ " and length " + str(length) + ". ")
     elif turtleIndex == 7:
          #draw CircularFractal
          pen.up(); pen.sety(-100); pen.down()
          turtlefigure.cr(order, length, pen)
          information.configure( text = "This is a Circular Fractal with order "
                               + str(order)+ " and length " + str(length) + ". ")
     elif turtleIndex == 8:
               #draw RhombusFlower
               pen.up(); pen.down()
               turtlefigure.rf(order, length, pen)
               information.configure( text = "This is a Rohmbus Flower with order "
                                    + str(order)+ " and length " + str(length) + ". ")


     elif turtleIndex == 9:
          #draw Spiral
          pen.up(); pen.down()
          turtlefigure.fs(order, length, pen)
          information.configure( text = "This is a Spiral with order "
                               + str(order)+ " and length " + str(length) + ". ")   
          
          
# end convertF
 
 
 
 
 
# ---------------- make the interface ---------------
 
# make all  components of root

label = Label(root, font = ("Helvetica", 12), text = "Welcome to Turtle Generator!", bg = "#B8D3F2", fg = "#30395a")
label.grid(row = 0, column = 0, columnspan = 4)
 



# ---make the contol frame--------

controlFrame = LabelFrame(root, font = ("Helvetica", 12), text = "Control", bg = "#4F8ACA", foreground = "#FFFFFF")
controlFrame.grid(row = 1, column = 5, rowspan = 2, columnspan = 3,  padx = 10, pady = 5, ipadx = 5, ipady = 5)

# order
orderLabel = ttk.Label(controlFrame, font = ("Helvetica", 12), text = " Order", width = 7, background = "#355d86", foreground = "white")
orderLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

 
orderStr = StringVar()
orderEntry = ttk.Entry(controlFrame, textvariable = orderStr)
orderEntry.grid(row=0, column = 1)

figureLabel = ttk.Label(controlFrame, font = ("Helvetica", 12), text = " Figure", width = 7, background = "#355d86", foreground = "white")
figureLabel.grid(row = 2, column = 0, padx = 10, pady = 10)

# length  
lengthLabel = ttk.Label(controlFrame, font = ("Helvetica", 12), text = "Length",width = 7, background = "#355d86", foreground = "white")
lengthLabel.grid(row = 1, column = 0, padx = 10, pady = 10)
 
lengthStr = StringVar()
lengthEntry = ttk.Entry(controlFrame, textvariable = lengthStr)
lengthEntry.grid(row = 1, column = 1)
 

# make combobox
figureList = ["Binary Tree", "Quad Tree", "Fern Tree","Serpinsky Gasket", "Koch Curve","Snowflake", "Anti-Snowflake", "Circular Fractal", "Rhombus Flower","Spiral"]
figureStr = StringVar()

combobox = ttk.Combobox(controlFrame, textvariable = figureStr, state="readonly")
combobox["values"] = figureList
combobox.grid(row = 2, column = 1)
combobox.current()
combobox.set("Please select a figure.")

# draw button 
drawButton = Button(controlFrame, font = ("Helvetica", 12), text = "Draw", width = 7, bg = "#355d86", fg = "#FFFFFF", command = onDrawF)
drawButton.grid(row = 3, column = 0, padx = 20, pady = 10)

# clear button 
clearButton = Button(controlFrame, font = ("Helvetica", 12), text = "Clear", width = 7, bg = "#355d86", fg = "#FFFFFF", command = onClearF)
clearButton.grid(row = 3, column = 1)
 
# ----------make the canvas-------------
canvasFrame = LabelFrame(root, font = ("Helvetica", 12), text = "Canvas", background = "#B8D3F2" , foreground = "#355d86")
canvas = Canvas(canvasFrame, width = 420, height = 400, bg = "#30395A")
canvas.pack()
canvasFrame.grid(row = 1, column = 0, rowspan = 4, columnspan = 4, padx = 10, pady = 10, ipadx = 5, ipady = 5)



#-----------control the pen---
pen = turtle.RawTurtle(canvas)
pen.color("#355d86")
pen.speed(0)
pen.width(3)

# Information frame-----
informationFrame = LabelFrame(root, width = 200, height = 60, font = ("Helvetica", 12), text = "Information",
                              background = "#B8D3F2", foreground = "#355d86")
informationFrame.grid(row = 3, column = 5,
                  rowspan = 3, columnspan = 5,
                 padx = 10, pady = 5, ipadx = 5, ipady = 5)


#Create the Message
information = Message(informationFrame, width = 200,
                        background = "#B8D3F2", foreground = "#355d86",
                      font = ("Helvetica", 12), text = "This is a panel of information.")
information.pack()


          










