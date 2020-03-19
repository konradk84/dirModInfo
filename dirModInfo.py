import os
import sys
import os.path, time
from datetime import datetime, timedelta

def getUserParams():
    if len(sys.argv) < 2:
        print('''\nToo few arguments. Params <folder_path> <days>''')
        exit()
    else:
        return sys.argv


def check_date(file,log,oneHourAgo,days):
    #oneHourAgo = datetime.now().strftime("%c")
    #days =  datetime.strptime(days, '%c')
    oneHourAgoObj = datetime.strptime(oneHourAgo, '%c') - timedelta(days=int(days))
    fileDateObj = oneHourAgoObj - timedelta(days=int(days))
    fileDate = time.ctime(os.path.getmtime(file))
    fileDateObj = datetime.strptime(fileDate, '%c')
    #print(fileDateObj)
    #print("godzina temu: ", oneHourAgoObj)
    if fileDateObj > oneHourAgoObj:
        print("modyfikacja: ", file," ", fileDateObj)
        log.write("modyfikacja: " + "\n" + file + " " + str(fileDateObj) + "\n\n")
        #else:
            #print("starszy")

getUserParams()            
folder_path = sys.argv[1]
days = sys.argv[2]
oneHourAgo = datetime.now().strftime("%c")
log = open("log", "w", encoding="utf-8")
#log = open("/././ftp/zmiany.txt", "w", encoding="utf-8")
print("przeszukiwanie rozpoczęte\n")
log.write("przeszukiwanie rozpoczęte: " + oneHourAgo + "\n\n")
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
            check_date(file,log,oneHourAgo,days)
        except UnicodeEncodeError:
            print("UnicodeEncodeError")
            log.write("UnicodeEncodeError\n")
print("\nprzeszukiwanie zakończone")
log.write("\nprzeszukiwanie zakończone\n\n")
log.close()
