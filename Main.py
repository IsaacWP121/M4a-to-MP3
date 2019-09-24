import os, pydub, subprocess # importing libraries
path = "F\\" # Selecting the path (in this case a usb drive)
os.chdir(path) # change the path
files = [] # creating a list variable for all the qualifying file's names and extentions will be indexed
names = [] # creating a list for just the names, not needed but helps my brain
            
def yes(): # defining a function were it removes the mp4 after conversion
    for r, d, f in os.walk(path): # setting a for loop for with an iteration for every file (f) in os.walk(path)
        for file in f: # setting a for loop for every file 
            if '.m4a' in file: # if the string of file -which is something like example.py- contains ".m4a"
                files.append(file) # it will add the full name of the file to the files list
                names.append(file.replace(".m4a", "")) # it will add just the file name without the extention to the names list

    for i in range(len(files)): # sets a for loop with an iteration for every item in the files list
            subprocess.call('cls',shell=True) # clears the window so that it is blank
            print("--Working on " + (str(i+1)) + " of " + str(len(files)) + "--") # printing out --Working on "x" of "y"-- where x is the current file and y is total files
            song = pydub.AudioSegment.from_file(files[i]) # sets song variable with a value of the raw audio as extracted by pydub 
            song.export(names[i] + ".mp3", format="mp3") # exports song variable with the apropriete name and the mp3 extention
            os.remove(files[i]) # removes the old m4a file
            
	
def no():
    for r, d, f in os.walk(path): # setting a for loop for with an iteration for every file (f) in os.walk(path)
        for file in f: # setting a for loop for every file 
            if '.m4a' in file: # if the string of file -which is something like example.py- contains ".m4a"
                files.append(file) # it will add the full name of the file to the files list
                names.append(file.replace(".m4a", "")) # it will add just the file name without the extention to the names list

    for i in range(len(files)): # sets a for loop with an iteration for every item in the files list
            subprocess.call('cls',shell=True) # clears the window so that it is blank
            print("--Working on " + (str(i+1)) + " of " + str(len(files)) + "--") # printing out --Working on "x" of "y"-- where x is the current file and y is total files
            song = pydub.AudioSegment.from_file(files[i]) # sets song variable with a value of the raw audio as extracted by pydub 
            song.export(names[i] + ".mp3", format="mp3") # exports song variable with the apropriete name and the mp3 extention

if __name__ == "__main__":
    yes() #change to no if you don't want to delete the m4a's from the path
