#Guess the Number 

import random

class Number:    
    def GuessWhat(self, Min_Number, Max_Number):
        self.Min_Number = Min_Number
        self.Max_Number = Max_Number 
        # input to start the game 
        play = input("want to play a guessing game? ")
        
        #Game Loops on yes input 
        while play.lower() == "yes":
            #Random number is generated 
            rand = random.randint(Min_Number, Max_Number)
            
            #Player chooses numbers 0 - 10 
            answer = input("Guess a number between 1 - 2: ")
            
            #Random number is revealed to player 
            print(f"The real answer is {rand}")
        
            #Successful reaction to correct guess. Restarts loop on play == yes 
            if len(answer) == rand:
                print(f"Great job! You got the answer {rand} correct. Hoorahh")
                play = input("Want to play the guessing game? ")
            
            #not so successful reaction to a bad guess. Restarts loop on play == yes 
            else:
                print(f"not even close you got {rand} wrong... Yikes, your answer was {answer}")
                play = input("Want to play the guessing game? ")
            
        else: #If play == "anything other than yes" closes loop 
            print("Play some other time.")
                
            
answer = " "
play = " "

g1 = Number()
g1.GuessWhat(Min_Number=1,Max_Number=2)
