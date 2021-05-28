#Python program to check if directory exists, if not, it will create a new one
import os
import time
from datetime import datetime

dt = datetime.now()
parent_dir = r"C:\Users\Public\Desktop"

try:
    #format for the Yearly directory name
    yearlyfolder = time.strftime("%Y")
    datepath = dt.strftime("\\")
    path = os.path.join(parent_dir+datepath, yearlyfolder) 
    os.mkdir(path) 
    print("Directory '% s' created" % yearlyfolder)
except:
    print("Directory '% s' already exists" % yearlyfolder)



try:
    #format for the Monthly directory name
    monthlyfolder = time.strftime("%m-%b")
    datepath = dt.strftime("\\%Y\\")
    path = os.path.join(parent_dir+datepath, monthlyfolder) 
    os.mkdir(path) 
    print("Directory '% s' created" % monthlyfolder)
except:
    print("Directory '% s' already exists" % monthlyfolder)



try:
    #format for the Daily directory name
    dailyfolder = time.strftime("%#m-%#d-%y")
    datepath = dt.strftime("\\%Y\\%m-%b\\")
    path = os.path.join(parent_dir+datepath, dailyfolder) 
    os.mkdir(path) 
    print("Directory '% s' created" % dailyfolder)
except:
    print("Directory '% s' already exists" % dailyfolder)
