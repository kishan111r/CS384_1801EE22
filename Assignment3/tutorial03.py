import csv
import os
import string
os.system("clear")
# header = ['id','full_name','country','email','gender','dob','blood_group','state']

def writeFile(file_name,item,header):
    flag=0
    if os.path.isfile(file_name):
        flag=1
    
    with open(file_name,mode= '+a') as file:
        writer = csv.writer(file)
        if(flag==0):
            writer.writerow(header)
        writer.writerow(item)
    file.close()



def course():
    # Read csv and process
    #print(os.getcwd())
    with open("studentinfo_cs384.csv",'r') as file:
        my_file = csv.DictReader(file,delimiter=',',skipinitialspace=True)
        next(my_file)
        for row in my_file:
            data = list(row.values())
            header = list(row.keys())
            roll_no = row['id']
            year = str(roll_no[0:2])
            stream_code = str(roll_no[2:4])
            branch = str(roll_no[4:6])
            serial = str(roll_no[6:8])
            #file_name = "misc.csv"

            general_path = os.getcwd()
            analytics_path = os.path.join(general_path,'analytics')
            if(os.path.exists(analytics_path)==False):
                os.mkdir(analytics_path)
            course_path= os.path.join(analytics_path,'course')
            if(os.path.exists(course_path)==False):
                os.mkdir(course_path)
            
            if not (year.isdigit() and stream_code.isdigit() and branch.isalpha() and serial.isdigit() and len(roll_no)==8):
                misc_path = os.path.join(course_path,'misc.csv')
                writeFile(misc_path,data,header)
                continue
                # if(n>30):
                #     break

            branch=branch.lower()
            branch_path = os.path.join(course_path,branch)
            if(os.path.exists(branch_path)==False):
                os.mkdir(branch_path)
            # print(stream_code)
            # break
            #stream=''
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
            file_name= year+'_'+branch+'_'+stream+".csv"
            file_path=os.path.join(stream_path,file_name)
            writeFile(file_path,data,header)
            
    file.close()
    



            
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

