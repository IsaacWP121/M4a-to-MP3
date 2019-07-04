import os, pydub, subprocess, time
path = "F\\"
os.chdir(path)
files = []
names = []
            
def yes():
    for r, d, f in os.walk(path):
        for file in f:
            if '.m4a' in file:
                files.append(file)
                names.append(file.replace(".m4a", ""))

    for i in range(len(files)):
            subprocess.call('cls',shell=True)
            print("--Working on " + (str(i+1)) + " of " + str(len(files)) + "--")
            song = pydub.AudioSegment.from_file(files[i])
            song.export(names[i] + ".mp3", format="mp3")
            os.remove(files[i])
            
	
def no():
    for r, d, f in os.walk(path):
        for file in f:
            if '.m4a' in file:
                files.append(file)
                names.append(file.replace(".m4a", ""))

    for i in range(len(files)):
            subprocess.call('cls',shell=True)
            print("--Working on " + (str(i+1)) + " of " + str(len(files)) + "--")
            song = pydub.AudioSegment.from_file(files[i])
            song.export(names[i] + ".mp3", format="mp3")

if __name__ == "__main__":
    yes() #change to no if you don't want to delete the m4a's from the path
