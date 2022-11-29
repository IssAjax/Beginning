# Write to a file on my desktop 
import os
from pathlib import Path
#Current working directory  
cwd = Path.cwd()
print(cwd)

#Set the file path 
file = Path().resolve()/"C:\\Users\\dantae.hudson\\Desktop\\test.txt"

#This allows me to create the file 
create_file = open(file, "x")
create_file.close()
#This has allowed me to overwrite exiting data from the file "test.txt" 
write_to_file = open(file, "w")

write_to_file.write("Here is a new data and new file update.")
write_to_file.close()

#This lets me read what is in the file 
read_file = open(file, "r")
print(read_file.read())
read_file.close()

#This will allow me to add to the file leaving the old text still in tact. 

append_to_file = open(file, "a")
append_to_file.write("\nThis is all new to me I can now append to the file. \nThis is a new line added to the file.")
append_to_file.close()

#reading what i just added to the file 
read_file = open(file, "r")
print(read_file.read())
read_file.close()

#now that all is said and done I would like to remove the file 

if Path.exists(file):
    os.remove(file)
    print("File Has been removed.")

else:
    print("File Does not exist.")