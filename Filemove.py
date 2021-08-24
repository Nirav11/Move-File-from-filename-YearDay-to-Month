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

  



# for f in os.listdir("folder"):
#     print(os.path.join('folder', f))

#     if not os.path.exists(folderName):
#         os.mkdir(folderName)
#         shutil.copy(os.path.join('folder', f), folderName)
#     else:
#         shutil.copy(os.path.join('folder', f), folderName)



### WORKING ##
# from datetime import datetime 


# data = ['2010001', '2010112', '2010365']

# for s in data:
#     dt = datetime.strptime(s, '%Y%j')
#     print(dt.monthStamp)


### PARTIALLY WORKING ##
# dt = [datetime.strptime(s, '%Y%j') for s in data]
# print(dt.monthStamp)