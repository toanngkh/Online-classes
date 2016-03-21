# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

rangex = 100

# helper function to start and restart the game
def new_game():
    """ Reset secret number, print out 'New game' """
    global secret_number
    global life
    
    if rangex == 100:	#game starts or range100 is chosen 
        secret_number = random.randrange(100)
        life = 7
        print "New game. Range is from 0 to 100"
    elif rangex == 1000:	#range1000 is chosen
        secret_number = random.randrange(1000)
        life = 10
        print "New game. Range is from 0 to 1000"
    
    print "Number of remaining guesses is", life
       
# define event handlers for control panel
def range100():
    global rangex
    rangex = 100
    new_game()
    
def range1000():
    global rangex
    rangex = 1000
    new_game()
    
def input_guess(text):	# event handler to get input text
    global life
        
    numb = int(text)
    life -= 1
    print
    print "Guess was", numb
    print "Number of remaining guesses is", life
    
    if life > 0 and numb != secret_number:
        if numb > secret_number:
            print "Lower!"
        elif numb < secret_number:
            print "Higher!"
    elif life >= 0 and numb == secret_number:
        print "Correct"
        print
        new_game()
    elif life == 0:
        print "You ran out of guesses. The number was", secret_number
        print
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements and start frame
frame.add_input("Input number", input_guess, 100)
frame.add_button("Range is [0, 100)", range100, 100)
frame.add_button("Range is [0, 1000)", range1000, 100)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
