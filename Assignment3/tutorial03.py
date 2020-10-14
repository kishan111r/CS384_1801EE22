import csv
import os
import string
os.system("clear")
# try:
#     os.rmdir('analytics')
# except:

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

course()

def country():
    # Read csv and process
    with open("studentinfo_cs384.csv",'r') as file:
        my_file = csv.DictReader(file,delimiter=',',skipinitialspace=True)
        next(my_file)
        for row in my_file:
            data = list(row.values())
            header = list(row.keys())
            my_nation = row['country']
            general_path = os.getcwd()
            analytics_path = os.path.join(general_path,'analytics')
            if(os.path.exists(analytics_path)==False):
                os.mkdir(analytics_path)
            country_path = os.path.join(analytics_path,'country')
            if(os.path.exists(country_path)==False):
                os.mkdir(country_path)
            if(len(my_nation)==0):
                file_name="misc.csv"
                file_dir=country_path+file_name
                writeFile(file_dir,data,header)
                continue
            file_name = row['country'].lower()+'.csv'
            country_file = os.path.join(country_path,file_name)
            writeFile(country_file,data,header)

    file.close()

country()
def email_domain_extract():
    # Read csv and process
    with open("studentinfo_cs384.csv",'r') as file:
        my_file = csv.DictReader(file,delimiter=',',skipinitialspace=True)
        next(my_file)
        for row in my_file:
            data = list(row.values())
            header = list(row.keys())
            email_id = row['email']
            # Domain name extraction
            domain=''
            if('@'in email_id and '.'in email_id):
                domain_half=email_id.split('@')[1]
                domain=domain_half.split('.')[0]
            domain=domain.lower()
            general_path = os.getcwd()
            analytics_path = os.path.join(general_path,'analytics')
            if(os.path.exists(analytics_path)==False):
                os.mkdir(analytics_path)
            email_path = os.path.join(analytics_path,'email_domain')
            if(os.path.exists(email_path)==False):
                os.mkdir(email_path)
            if(len(domain)==0):
                file_name="misc.csv"
                file_dir=email_path+file_name
                writeFile(file_dir,data,header)
                continue
            file_name = domain+'.csv'
            domain_file = os.path.join(email_path,file_name)
            writeFile(domain_file,data,header)
    file.close()
email_domain_extract()
def gender():
    # Read csv and process
    with open("studentinfo_cs384.csv",'r') as file:
        my_file = csv.DictReader(file,delimiter=',',skipinitialspace=True)
        next(my_file)
        for row in my_file:
            data = list(row.values())
            header = list(row.keys())
            gender = row['gender']
            gender= gender.lower()
            # Domain name extraction
            general_path = os.getcwd()
            analytics_path = os.path.join(general_path,'analytics')
            if(os.path.exists(analytics_path)==False):
                os.mkdir(analytics_path)
            gender_path = os.path.join(analytics_path,'gender')
            if(os.path.exists(gender_path)==False):
                os.mkdir(gender_path)
            if(len(gender)==0):
                file_name="misc.csv"
                file_dir=gender_path+file_name
                writeFile(file_dir,data,header)
                continue
            file_name = gender+'.csv'
            gender_file = os.path.join(gender_path,file_name)
            writeFile(gender_file,data,header)

    file.close()

gender()
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

