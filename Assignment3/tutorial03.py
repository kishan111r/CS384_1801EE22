import csv
import os
import string
os.system("clear")
header = ['id','full_name','country','email','gender','dob','blood_group','state']

def writeFile(file_name,item):
    flag=0
    if os.path.isfile(file_name):
        flag=1
    
    with open(file_name,'w') as file:
        writer = csv.writer(file)
        if(flag==0):
            writer.writerow(header)
        writer.writerow(item)



def course():
    # Read csv and process
    #print(os.getcwd())
    with open("studentinfo_cs384.csv",'r') as file:
        my_file = csv.reader(file,delimiter=',',skipinitialspace=True)
        next(my_file)
        for row in my_file:
            roll_no = row[0]
            year = roll_no[0:2]
            stream_code = roll_no[2:4]
            branch = roll_no[4:6]
            serial = roll_no[6:8]
            file_name = "misc.csv"
            if year.isdigit() and stream_code.isdigit() and branch.isalpha() and serial.isdigit() and len(roll_no)==8:
                # path_misc= os.path.join(os.getcwd(),"analytics/course")
                # os.chdir(path_misc)
                # writeFile(file_name,row)
                continue

            branch=branch.lower()
            general_path = os.getcwd()
            branch_path = os.path.join(general_path,"analytics/course")
            # branch_path = general_path+"/analytics/course"
            #print(branch_path)
            branch_path = os.path.join(branch_path,branch)
            if(os.path.exists(branch_path)==False):
                os.mkdir(branch_path)
            stream=''
            if(stream_code=='01'):
                stream = 'btech'
            elif(stream_code=='11'):
                stream='mtech'
            elif (stream_code=='12'):
                stream = 'msc'
            elif(stream_code=='21'):
                stream = 'phd'
            stream_path =os.path.join(branch_path,stream)
            if(os.path.exists(stream_path)==False):
                os.mkdir(stream_path)
            os.chdir(stream_path)
            file_name= year+'_'+branch+'_'+stream+".csv"
            writeFile(file_name,row)
            os.chdir("../../../..")


            
    pass

course()
def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

