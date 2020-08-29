"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

all_scores = []
 

def start_game():
    """Psuedo-code Hints
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function
    print("""
    -------------------------------------
    Welcome to the Number Guessing Game!
    -------------------------------------
    """)
    play_again = "yes"
    
    while play_again.lower() != "no":
      attempt = 1
      random_number = random.randint(1, 10)
      guess = None
      play_again = "no"
      
      while guess != random_number:
        try:
          guess = int(input("Pick a number between 1 and 10: "))
        except ValueError:
          print("Sorry wrong value! Try again!")
        else:
          if guess > random_number :
            print("It is lower")
            attempt += 1 
                
          elif guess < random_number :
            print("It is higher")
            attempt += 1
                   
          
          elif guess == random_number :
            print("You got it! It took {} tries.".format(attempt))
            all_scores.append(attempt)
            play_again = input("Would you like to play again? [Y]es/[N]o? ")
            print("Hiscore is {}".format(min(all_scores)))
          
    else:
      if play_again.lower() == "no": 
        print("Closing Game! See you next time!")
    

              
# Kick off the program by calling the start_game function.
start_game()