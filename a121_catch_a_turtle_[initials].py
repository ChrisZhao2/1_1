# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
spot = trtl.Turtle()

#-----game configuration----
spot.fillcolor("red")
spot.begin_fill()
spot.circle(50)
spot.end_fill()

#-----initialize turtle-----

#-----game functions--------
def spot_clicked(x,y):
  print("Spot was clicked!")

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()