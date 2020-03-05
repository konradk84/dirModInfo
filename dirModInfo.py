import os
import sys
import os.path, time
from datetime import datetime, timedelta

def sprawdz(file,f,oneHourAgo):
    #oneHourAgo = datetime.now().strftime("%c")
    oneHourAgoObj = datetime.strptime(oneHourAgo, '%c') - timedelta(minutes=60)
    fileDateObj = oneHourAgoObj - timedelta(minutes=60)
    fileDate = time.ctime(os.path.getmtime(file))
    fileDateObj = datetime.strptime(fileDate, '%c')
   

    #print(fileDateObj)
    #print("godzina temu: ", oneHourAgoObj)
    if fileDateObj > oneHourAgoObj:
        print("modyfikacja: ", file," ", fileDateObj)
        f.write("modyfikacja: " + file + " " + str(fileDateObj) + "\n")
        #else:
            #print("starszy")
            
folder_path = sys.argv[1]
oneHourAgo = datetime.now().strftime("%c")
f = open("/root/log", "a")
print("przeszukiwanie rozpoczęte")
f.write("przeszukiwanie rozpoczęte: " + oneHourAgo + "\n\n")
#print("zmodyfikowany lub dodany w ciagu ostatniej godziny: ")
for root, dirs, files in os.walk(folder_path, topdown=True):
    #for name in dirs:
    #    directory = os.path.join(root, name)
    #    print("dir: ", directory)
    for name in dirs:
        file = os.path.join(root, name)
        try:
            #print(file)
            #f.write(file)
            
            sprawdz(file,f,oneHourAgo)
        except UnicodeEncodeError:
            print("UnicodeEncodeError")
            f.write("UnicodeEncodeError\n")
print("przeszukiwanie zakończone")
f.write("\nprzeszukiwanie zakończone\n\n")
f.close()
