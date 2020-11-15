import csv
import os
import re
import shutil
import pandas as pd

current_path = os.getcwd()
delete_path = os.path.join(current_path, 'grades')
max_sem_no={}
# Function to delete the folders if it exist do that replica is not made and we can everytime make a new folder.
def del_grades_folder():
    if os.path.isdir(delete_path):
        shutil.rmtree(delete_path)  #Use of shutill Library to delete the whole tree.
    #New Folder
    os.mkdir(delete_path)


def roll_number_individual_result():
    try:
        grades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'F', 'I'] # Valid Grades of the Students in a Semester Grades 
        with open('acad_res_stud_grades.csv') as data_file:
            data_reader = csv.DictReader(data_file)
            for row in data_reader:
                roll_no = row['roll']
                max_sem_no[roll_no] = row['sem']
                current_path=os.getcwd()
                folder_path = os.path.join(current_path, 'grades')
                file_name = roll_no + '_individual.csv'
                file_path = os.path.join(folder_path, file_name)
                data_entry = {'Subject': row['sub_code'], 'Credits': row['total_credits'],
                              'Type': row['sub_type'], 'Grade': row['credit_obtained'], 'Sem': row['sem']}
                if data_entry['Grade'] in grades:
                    if os.path.isfile(file_path):
                        #If file already exist then the entry will be in append mode
                        try:
                            with open(file_path, mode='a+', newline='') as write_file:
                                data_writer = csv.DictWriter(write_file, fieldnames=['Subject', 'Credits', 'Type', 'Grade', 'Sem'])
                                #Ignored the time stamp and the serial number rows.
                                data_writer.writerow(data_entry)
                                write_file.close()
                        except:
                            print(f"There is some error opening the File:- {file_name} to write roll no :{row['roll']}")
                    else:
                        try:
                            with open(file_path, 'a+', newline='') as write_file:

                                #Creating the fresh file and writing the individual rows for meeting the template file.
                                write_file.write(f'Roll: {roll_no}\n')
                                write_file.write('Semester Wise Details\n')
                                writer = csv.DictWriter(write_file, fieldnames=['Subject', 'Credits', 'Type', 'Grade', 'Sem'])
                                writer.writeheader() #to write the header of the file
                                writer.writerow(data_entry) #To write the rows accumulated
                                write_file.close()
                        except:
                            print(f"There is some error opening the File:- {file_name} to write roll no :{row['roll']}")
               #If the Grades are Miscellaneous then it has to be placed in the misc file for Further processing
                else:
                    fieldname = ['sl', 'roll', 'sem', 'year', 'sub_code',
                                 'total_credits', 'credit_obtained', 'timestamp', 'sub_type']
                    file_name = 'misc.csv'
                    file_path = os.path.join(folder_path,file_name)
                    if os.path.isfile(file_path):
                        # opening file in append mode, then writing the current row, with header
                        try:
                            with open(file_path, 'a+', newline='') as write_file:
                                writer = csv.DictWriter(
                                    write_file, fieldnames=fieldname)
                                writer.writerow(row)
                                write_file.close()
                        except:
                            print(f"There is some error opening the File:- {file_name} to write roll no :{row['roll']}")
                  #If File doesn't Exist then creating and writing the header and then the content
                    else:
                        try:
                            with open(file_path, 'a+', newline='') as write_file:
                                writer = csv.DictWriter(write_file, fieldnames=fieldname)
                                writer.writeheader()
                                writer.writerow(row)
                                write_file.close()
                        except:
                            print(f"There is some error opening the File:- {file_name} to write roll no :{row['roll']}")

    except:
        print("Error while opening acad_res_stud_grades.csv")

# Since we have already compile the students individual record now we can calculate the Overall performance of the student.


def roll_number_overallresult():
    folder_path = os.path.join(current_path, 'grades')
    grades = {'AA':10, 'AB':9, 'BB':8, 'BC':7, 'CC':6, 'CD':5, 'DD':4, 'F':0, 'I':0} # Valid Grades of the Students in a Semester Grades
    os.chdir(folder_path)
    for ind_file in os.listdir(folder_path):
        if str(ind_file) != 'misc.csv':
            file_n = re.split('_', str(ind_file), maxsplit=1)
            roll_no = file_n[0]
            if(file_n[1] == 'overall.csv'):
                continue
            else:
                data_frame = pd.read_csv(ind_file, skiprows=2) #Used Pandas for modifing and working for result generation.
                data = dict(data_frame)
                Gr = list(data['Grade'])
                i = 0
                backlog = []
                for grade in Gr:
                    if grade == 'F':
                        backlog.append(i-1)
                    elif grade == 'I':
                        backlog.append(i-1)
                    i += 1
                sem_no = set(data_frame['Sem'])
                #print(backlog)
                keys = list(sem_no)
                sem = {}
                semwise_score = {}
                semwise_total_credits = {}
                semwise_credit_cleared = {}
                total_credits = {}
                total_credits_cleared = {}
                SPI = {}
                CPI = {}
                for key in keys:
                    try:
                        sem[key] = key
                        semwise_score[key] = 0
                        semwise_total_credits[key] = 0
                        semwise_credit_cleared[key] = 0
                        SPI[key] = 0
                        CPI[key] = 0
                        total_credits[key] = 0
                        total_credits_cleared[key] = 0
                    except:
                        print(f"There is some error roll no :{row['roll']}")
                i = 0
                for value in data_frame['Sem']:
                    try:
                        # if(data_frame['Grade'][i]=='F'):
                        #     backlog.append
                        semwise_score[value] += grades[data_frame['Grade'][i]]*data_frame['Credits'][i]
                        if data_frame['Grade'][i] != 'F' and data_frame['Grade'][i] != 'I':
                            semwise_credit_cleared[value] += data_frame['Credits'][i]
                        semwise_total_credits[value] += data_frame['Credits'][i]

                    except:
                        print(f"There is some error roll no :{row['roll']}")
                    i += 1
                for key in keys:
                    try:
                        if semwise_credit_cleared[key] != 0:
                            SPI[key] = round(semwise_score[key] /
                                             semwise_total_credits[key], 2)
                        else:
                            SPI[key] = 0
                    except:
                        print(f"There is some error")
                i = 0
                for key in keys:
                    try:
                        if i == 0 and i not in backlog:
                            total_credits[key] = semwise_total_credits[key]
                            total_credits_cleared[key] = semwise_total_credits[key]
                            x = total_credits[key]
                            y = total_credits_cleared[key]
                        elif i == 0 and i in backlog:
                            total_credits[key] = semwise_total_credits[key]
                            total_credits_cleared[key] = 0
                            x = total_credits[key]
                            y = total_credits_cleared[key]
                        elif i not in backlog:
                            total_credits[key] += (semwise_total_credits[key] + x)
                            total_credits_cleared[key] += (
                                semwise_total_credits[key] + y)
                            x = total_credits[key]
                            y = total_credits_cleared[key]
                        elif i in backlog:
                            total_credits[key] += (semwise_total_credits[key] + x)
                            x = total_credits[key]
                            total_credits_cleared[key] = y
                    except:
                        print(f"There is some error for roll no :{row['roll']}")
                    i += 1
                i = 0
                for key in keys:
                    try:
                        x = 0
                        y = 0
                        for j in sem:
                            if int(j)<=int (key):
                                x += SPI[j]*semwise_total_credits[j]
                        if total_credits[key] != 0:
                            y = x/total_credits[key]
                        else:
                            y = 0
                        CPI[key] = round(y, 2)
                        i += 1
                    except:
                        print(f'Error occured while working on -> {ind_file}')
                data_entry = []
                for key in range(1,int(max_sem_no[roll_no])+1):
                    if(key in keys):
                        l = [sem[key], semwise_total_credits[key], semwise_credit_cleared[key], SPI[key], total_credits[key], total_credits_cleared[key], CPI[key]]
                    else:
                        l=[key,0,0,0,0,0,0]
                    data_entry.append(l)
                file_name = roll_no + '_overall.csv'
                file_path = os.path.join(folder_path, file_name)
                for row in data_entry:
                    if os.path.isfile(file_path):
                        # opening file in append mode, then writing the current row, with header
                        try:
                            with open(file_path, 'a+', newline='') as write_file:
                                writer = csv.writer(write_file)
                                writer.writerow(row)
                                write_file.close()
                        except:
                            print(f"Error opening {file_name}")
                    else:
                        try:
                            with open(file_path, 'a+', newline='') as write_file:
                                write_file.write(f'Roll: {roll_no}\n')
                                writer = csv.writer(write_file)
                                fieldnames = ['Semester', 'Semester Credits', 'Semester Credits Cleared', 'SPI', 'Total Credits', 'Total Credits Cleared', 'CPI']
                                writer.writerow(fieldnames)
                                writer.writerow(row)
                                write_file.close()
                        except:
                            print(f"There is some error opening the File:- {file_name} to write roll no :{row['roll']}")







del_grades_folder()
roll_number_individual_result()
roll_number_overallresult()