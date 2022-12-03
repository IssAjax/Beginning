import os 
import logging

#print(f" You are currently working in the {os.getcwd()} directory.")
#Username = os.getlogin()
#print(f" You are currently logged in as {Username}")
class Move:
    
    def __init__(self, source_dir, target_dir, User): #constructor
        self.source_dir = source_dir 
        self.target_dir = target_dir
        self.User = User
        logging.basicConfig(filename=r"C:\Users\Dantae\Desktop\Python Scripts\logfile.log", level=20, format="%(levelname)s;%(asctime)s;%(message)s")


        #os.chdir(r".\Desktop")
    #Retrieves current user that is logged in 


    
    #This class method will allow no input from the program to work, it will be based off of the users input. 
    @classmethod
    def user_input(cls):
        print(f" You are currently working in the {os.getcwd()} directory.")
        source_dir = os.getcwd() + input("Where is the file(s) you wish to move? (Start with a \) ") + "\\"
        target_dir = os.getcwd() + input("Where do you want the file(s) to go? (Start with a \) ") + "\\"
        User = os.getlogin()
        return cls(source_dir, target_dir, User)
    #I wish to log what is going on 
#    @classmethod
#    def log_file(cls):
#        move_log = logging.basicConfig(filename="logfile.log", level=logging.DEBUG, format="%(levelname)s;%(asctime)s;%(message)s")
#        return cls.move_log
                            

    def file_move(self):
        print(self.source_dir)
        print(self.target_dir)
        print(self.User)
        
        # This beginning for kind of made the files a list of lists and had to add another for loop to take the file out of the list 
        # The prints were so that i can see when the file was taken out of the list's 
        amount = 0
        for path, dir, files in os.walk(self.source_dir):
            print(files)

                # As a fail safe this asks if you're sure you want the files to be transferred over.
            answer = input("Knowing the files in this location are you sure you want to move them? ")
            if answer.lower() == "yes":

                for file in files:

                        #This will count the files in the directory 
                    if os.listdir(self.source_dir):
                        amount = amount + 1

                        # Used try to test it on the single file before attempting a mass merge of files. 
                    try:
                        os.rename(path + "\\" + file, self.target_dir + file)
                        logging.info(f"files were moved susccessful. {amount} were transferred to {self.target_dir}. By {self.User}")
                        print("done")
                        
                
                    except:
                        logging.info(f"The files failed to move to {self.target_dir}. By {self.User}")
                        
            else:
                print("exiting movement script...")
#logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(levelname)s;%(asctime)s;%(message)s")
os.chdir(r"../")
M = Move.user_input()
M.file_move()
