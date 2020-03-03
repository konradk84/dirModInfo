import os
import sys
import os.path, time
from datetime import datetime, timedelta

def sprawdz(file):
    oneHourAgo = datetime.now().strftime("%c")
    oneHourAgoObj = datetime.strptime(oneHourAgo, '%c') - timedelta(minutes=60)

    fileDateObj = oneHourAgoObj - timedelta(minutes=60)
    fileDate = time.ctime(os.path.getmtime(file))
    fileDateObj = datetime.strptime(fileDate, '%c')

    print(file," ", fileDateObj)
    #print("godzina temu: ", oneHourAgoObj)
    if fileDateObj > oneHourAgoObj:
        print("nowszy")
    #else:
        #print("starszy")
        
folder_path = sys.argv[1]
for root, dirs, files in os.walk(folder_path, topdown=True):
    for name in files:
        file = os.path.join(root, name)
        #print(file)
        sprawdz(file)
    for name in dirs:
        directory = os.path.join(root, name)
        #print(directory)
