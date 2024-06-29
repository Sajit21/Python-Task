print("""               /eeeeeeeeeee\ 
   /RRRRRRRRRR\ /eeeeeeeeeeeee\ /RRRRRRRRRR\ 
  /RRRRRRRRRRRR\|eeeeeeeeeeeee|/RRRRRRRRRRRR\ 
 /RRRRRRRRRRRRRR +++++++++++++ RRRRRRRRRRRRRR\ 
|RRRRRRRRRRRRRR ############### RRRRRRRRRRRRRR| 
|RRRRRRRRRRRRR ######### ####### RRRRRRRRRRRRR| 
 \RRRRRRRRRRR ######### ######### RRRRRRRRRR/ 
   |RRRRRRRRR ########## ######## RRRRRRRR| 
  |RRRRRRRRRR ################### RRRRRRRRR| 
               ######     ###### 
               #####       ##### 
               #nnn#       #nnn# """)
print("welcome to treasure")
choice=input("which way do you want to go? (left/right)").lower()
if(choice=="left"): #continue the process
    choice2=input("you've come to a lake.there is an island in the middle of the lake.type wait to wait for a boat.typw swim to swim across").lower()
    if(choice2=="wait"): #continue the process
      choice3=input("you arrive at island unharmed.there is a house with 3 doors.one red, one yellow and one blue.which color do you choose?").lower()
      if(choice3=="red"):
        print("it's a room full of fire.game over")
      elif(choice3=="yellow"):
       print("you found the treasure.you win")
      elif(choice=="blue"):
       print("you wnter a room of beast.game over")
      else:
       print("you choose a door that doesn't exist")

    else:
     print("\nyou got attacked bt an angry trout.game over")
else:
 print("you fell into a hole.game over")