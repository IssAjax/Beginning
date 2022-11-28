#Mad Libs project



class Story: 

    def Gen(self):
        #No identifiers needed because all is based off of user input. 

        answer = input("Would you like to tell a short story? ")


        #The story begins on a yes input from user 
        if answer.lower() == "yes":
            
            #questions and program initiates interest in user input 

            name = input("What is your name? ")
            print(f"{name} is a great name.")
            noun = input("Name a place: ")
            print(f"{noun} is oddly specific.")
            verb = input("Name an activity: ")
            print(f"Oh, you like {verb}.")
            adjective = input("What is a sport you an think of? ")
            print(f"{adjective} is a great sport.")


            #program asks users for confirmation they want to hear the sotry 

            ans1 = input("Is this the story you would like to go with? ")

            #if users says yes to the question it will print the story 

            if ans1.lower() == "yes":

                print("Okay, I think we have something here.")
                print(f"{name.upper()} was at {noun.upper()}, where {name.upper()} use to {verb.upper()} {adjective}")
            
            #Alternate "no" response if the user does not want to hear the story but made it through the questions 
            
            else:
                print("I would love to hear a story another time.")


        #Original "no" response if the user declines wanting to tell a short story  
        else:
            print("We can tell a story another time")


c1 = Story()
c1.Gen()