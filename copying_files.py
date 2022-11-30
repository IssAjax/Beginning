import os 

#Retrieves current user that is logged in 
Username = os.getlogin()
print(Username)

#change to a specific directory using relative path 
os.chdir(".\Desktop")
cwd = os.getcwd()
print(cwd)


#target_dir = r"C:\Users\dantae.hudson\Desktop\Folder" + "\\"
target_dir = cwd + r"\Folder" + "\\"
#source_dir = r"C:\Users\dantae.hudson\Desktop\Network Liaison stuff" + "\\"
source_dir = cwd + r"\Network Liaison stuff" + "\\"


# This beginning for kind of made the files a list of lists and had to add another for loop to take the file out of the list 
# The prints were so that i can see when the file was taken out of the list's 
amount = 0
for path, dir, files in os.walk(target_dir):
    print(files)

    # As a fail safe this asks if you're sure you want the files to be transferred over.
    answer = input("Knowing the files in this location are you sure you want to move them? ")
    if answer.lower() == "yes":

        for file in files:

            #This will count the files in the directory 
            if os.listdir(target_dir):
                amount = amount + 1
            print(amount)

            # Used try to test it on the single file before attempting a mass merge of files. 
            try:
                os.rename(path + "\\" + file, source_dir + file)
                print(f"files were moved susccessful. {amount} files were transferred to {source_dir}.")
    
            except:
                print("The move has failed")
    else:
        print("exiting movement script...")
