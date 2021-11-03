# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
spot = trtl.Turtle()
import random as rand
#-----game configuration----
spotshape="circle"
shapesize=10
spotcolor="red"
spot.shape()

#-----initialize turtle-----
spot.shape(spotshape)
spot.turtlesize(shapesize)
spot.fillcolor(spotcolor)
spot.speed(0)
spot.penup()
#-----game functions--------
def spot_clicked(x,y):
  size=rand.randint(1,10)
  change_position(size)
def change_position(size):
  new_xpos = rand.randint(0,400)
  new_ypos = rand.randint(0,300)
  colors = ["blue" , "red", "green", "pink"]
  colorcycle = rand.randint(0,3)
  spot.hideturtle()
  spot.fillcolor(colors[colorcycle])
  spot.turtlesize(size)
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()