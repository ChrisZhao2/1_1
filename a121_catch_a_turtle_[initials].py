# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
spot = trtl.Turtle()
import random as rand
#import leaderboard as lb
#-----game configuration----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
spotshape="circle"
shapesize=10
spotcolor="red"
spot.shape()


#-----initialize turtle-----
counter =  trtl.Turtle()
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(-200,250)

# leaderboard variables
""""
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")
"""
spot.shape(spotshape)
spot.turtlesize(shapesize)
spot.fillcolor(spotcolor)
spot.speed(0)
spot.penup()
#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
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
# manages the leaderboard for top 5 scorers
""""
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

"""
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()