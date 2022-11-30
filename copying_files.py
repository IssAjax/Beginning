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

for path, dir, files in os.walk(target_dir):
    print(files)
    for file in files:
        print(file)

        # Used try to test it on the single file before attempting a mass merge of files. 
        try:
            os.rename(path + "\\" + file, source_dir + file)
            print(f"The move was susccessful {files} now exist in {source_dir}")
    
        except:
            print("The move has failed")
    
