import os, shutil
from datetime import datetime
os.chdir("E:/Data")
folder = 'E:/Data'


for f in os.listdir("folder"):
    folderName = f[-11:-4]
    print(folderName)
    dateStamp = datetime.strptime(folderName, '%Y%j')
    monthStamp = str(dateStamp.monthStamp)
    print(monthStamp)
    if not os.path.exists(monthStamp):
        os.mkdir(monthStamp)
        shutil.copy(os.path.join('folder', f), monthStamp)
    else:
        shutil.copy(os.path.join('folder', f), monthStamp)

  



