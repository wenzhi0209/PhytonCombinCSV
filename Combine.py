import os, glob
import pandas as pd

### This code is using relative path, please put the .py file
### into the same directory of your Hotayi dataset main folder, or manually change all the path 

#CSV folder

#check path
mainfolder = "Result_MC1_2020_11"

files = os.listdir(mainfolder)
num_folder = len(files)     
print("Number of folder :" , num_folder)


# genearate day combined
#Change Day
# i start from 0

for i in range(num_folder):
    constr=str(i+1)
    if i < 9:
        constr="0"+constr
    #check path
    path= mainfolder+"/2020_11_"+constr+"/1234567890"
    files = os.listdir(path)
    num_file = len(files) 
    print("Number of file in folder ", i+1 ," : " , num_file)
    
    if not os.path.exists("DailyResult"):
        os.mkdir("DailyResult")


    print("Merging file 2020_11_"+constr)
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    df_merged   = pd.concat(df_from_each_file, ignore_index=True)
    #check path (output)
    df_merged.to_csv("DailyResult/2020_11_"+constr+".csv")
    print("done \n")


#Generate month combined
#check path (where is your daily combined)

print("\n\n ****Starting combine day result in a month**** \n")
combinedDayFolder = "DailyResult"

files = os.listdir(combinedDayFolder)
num_day_file = len(files)     
print("Number of Day file :" , num_day_file)


for i in range(num_day_file):
    constr=str(i+1)
    if i < 9:
        constr="0"+constr
    path= combinedDayFolder

    print("Merging all day file ", constr)
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    df_merged   = pd.concat(df_from_each_file, ignore_index=True)
    #check path (output)
    df_merged.to_csv("2020_11.csv")
    print("done all operation \n")


