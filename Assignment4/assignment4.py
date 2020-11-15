import csv
import os
import re
import shutil
import pandas as pd

current_path = os.getcwd()
delete_path = os.path.join(current_path, 'grades')

# Function to delete the folders if it exist do that replica is not made and we can everytime make a new folder.
def del_grades_folder():
    if os.path.isdir(delete_path):
        shutil.rmtree(delete_path)  #Use of shutill Library to delete the whole tree.
    #New Folder
    os.mkdir(delete_path)


def roll_number_individual_result():
    try:
        grades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'F', 'I']
        with open('acad_res_stud_grades.csv') as data_file:
            data_reader = csv.DictReader(data_file)
            for row in data_reader:
                roll_no = row['roll']
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

del_grades_folder()
roll_number_individual_result()
