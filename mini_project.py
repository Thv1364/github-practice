print("\n\n\n\n\n\n Project 3")
import random
comp=4

def rps(inp, comp):

  print("The computer got", comp)
 
  if inp==0 and comp==1:
    print("You lose!")

  elif inp==0 and comp==2:
    print("You win!")

  elif inp==1 and comp==0:
    print("You win!")

  elif inp==1 and comp==2:
    print("You lose!")

  elif inp==2 and comp==0:
    print("You lose!")

  elif inp==2 and comp==1:
    print("You win!")

  elif inp==comp:
    print("It's a tie!")
    

def play_game():
  
  
  a=0 #game modes, 0 is rigged, 1 is nice
  x=int(input("What is your favorite integer? \n"))
  if x==64:
    a=1

  inp=int(input("Rock (type 0), Paper (type 1), or Scissors (type 2)? \n"))
  
  if a==1: #standard nice
    print("Let's see how you do...")
    comp=random.randint(0,2)
    rps(inp, comp)
  
  else: #standard rigged
    print("Let's see how you do...")
    
    if inp==0:
      comp=1
    if inp==1:
      comp=2
    if inp==2:
      comp=0
    rps(inp, comp)
    
play_game()
