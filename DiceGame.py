# Dice Rolling Sim 
import random
class Dice:
        
    def Roll(self, Min_Number, Max_Number):
        self.Min_Number = Min_Number
        self.Max_Number = Max_Number
        
        #Random If Statement 
        if Max_Number > 6:
            print("What is this DnD?")
            
        while True:
            answer = input("Do you want to roll DICE? Yes or No: ")   
            
            
        #This will start the endless loop that is the dice game 
            while answer.lower() == "yes":
                print("you rolled a : ", random.randint(Min_Number, Max_Number))
                answer = input("Do you want to roll DICE? Yes or No: ")
            
            #This will end the game of dice if the answer is anything but yes 
            else: 
                print("Run the program to play another time")
                break
            
            
 
            
    
        
answer = " "
D1 = Dice()
D1.Roll(Min_Number=1,Max_Number=7)
