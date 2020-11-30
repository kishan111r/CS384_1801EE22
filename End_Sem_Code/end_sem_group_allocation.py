import os
import csv
import math
import pandas as pd
import shutil

def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
    # curr_dir =  os.getcwd()
    # os.path.join(curr_dir,filename)
    #Code to Delete existing File (if Any)
    dire = os.getcwd()
    group_folder = os.path.join(dire,'Group_Wise_Folder')
    if(os.path.isdir(group_folder)):
        shutil.rmtree(group_folder)
    os.mkdir(group_folder)
    branch_folder = os.path.join(dire,'Branch_Wise_Folder')
    if(os.path.isdir(branch_folder)):
        shutil.rmtree(branch_folder)
    os.mkdir(branch_folder)


    branch_wise_count = {}
    with open(filename,mode='r') as file:
        my_file = csv.DictReader(file,delimiter=',',skipinitialspace=True)
        for row in my_file:
            data = list(row.values())
            header = list(row.keys())
            roll_no = row["Roll"]
            branch_code = roll_no[4:6]
            branch_code=branch_code.upper()
            present_dir  =  os.getcwd()
            branch_folder = os.path.join(present_dir,"Branch_Wise_Folder")
            branch_file = os.path.join(branch_folder,branch_code+'.csv')
            if(branch_wise_count.get(branch_code)==None):
                # New branch is encontered so we have to add it in the file:
                if os.path.isfile(branch_file):
                        os.remove(branch_file)
                with open(branch_file,mode='a+') as write_file:
                    my_writer = csv.writer(write_file)
                    my_writer.writerow(header)
                branch_wise_count[branch_code]=0
            branch_wise_count[branch_code]+=1
            with open(branch_file,mode='a+') as write_file:
                    my_writer = csv.writer(write_file)
                    my_writer.writerow(data)
    my_file_name="branch_strength.csv"
    with open(my_file_name,mode='w',newline="") as file:
        my_writer = csv.writer(file)
        header = ["BRANCH CODE","STRENGTH"] 
        my_writer.writerow(header)
    file.close()
    count_in_descending = []
    for branch_code in branch_wise_count.keys():
        count_in_descending.append([branch_code, branch_wise_count[branch_code]])
    count_in_descending = sorted(count_in_descending, key=lambda l: int(l[1]), reverse=True) ## Sorting in descending order of the strength
    
    with open(my_file_name,mode="a+",newline="") as file:
        my_writer = csv.writer(file)
        for entries in count_in_descending:
            my_writer.writerow(entries)
    number_of_branches = len(branch_wise_count)  #Number of branches found while looking up the data

    #Building of the table
    # group_table=[[]]
    group_table = [[0 for i in range(number_of_branches+2)]
             for j in range(number_of_groups+1)]
    group_table[0][0] = "Group"
    group_table[0][1] = "Total"
    for i in range(2, number_of_branches+2):
        group_table[0][i] = count_in_descending[i-2][0]
    number_of_digits_in_gname = len(str(number_of_groups))
    for i in range(1, number_of_groups+1):
        number_of_zeroes2append = number_of_digits_in_gname-len(str(i))
        group_table[i][0] = "Group_G"+'0'*number_of_zeroes2append+str(i)+".csv"
    left_over_stud_in_each_branch = []
    for i in range(len(count_in_descending)):
        num_of_students_intitially = math.floor(count_in_descending[i][1]/number_of_groups)
        for j in range(1, number_of_groups+1):
            group_table[j][i+2] = num_of_students_intitially
        #Leftover students after the first round of the complete allocation
        left_over_stud_in_each_branch.append(count_in_descending[i][1]-number_of_groups*num_of_students_intitially)
    #Distribution
    allocated_num = 1
    for i in range(len(left_over_stud_in_each_branch)):
        while left_over_stud_in_each_branch[i] > 0:
            group_table[allocated_num][i+2] += 1
            left_over_stud_in_each_branch[i] -= 1
            if allocated_num == number_of_groups:
                allocated_num = 1
            else:
                allocated_num += 1
    for i in range(1, number_of_groups+1):
        for j in range(2, number_of_branches+2):
            group_table[i][1] += group_table[i][j]
    stats_file= 'stats_grouping.csv'
    #If the file Exist the delete and make a new file
    if os.path.isfile(stats_file):
        os.remove(stats_file)
    with open(stats_file, mode='w', newline="") as file:
        stats_writer = csv.writer(file)
        stats_writer.writerows(group_table) # Writing the rows of the table of the Groups
    for i in range(1, number_of_groups+1):
        present_dir  =  os.getcwd()
        branch_folder = os.path.join(present_dir,"Group_Wise_Folder")
        branch_file = os.path.join(branch_folder,group_table[i][0])
        with open(branch_file,mode='w', newline="") as file:
            header_writer = csv.writer(file)
            #Writing the header first to the newly created file
            header_writer.writerow(["Roll", "Name", "Email"])
    for i in range(2, number_of_branches+2):
        file_name_appended = group_table[0][i]+'.csv'
        present_dir  =  os.getcwd()
        branch_folder = os.path.join(present_dir,"Branch_Wise_Folder")
        file_name_appended = os.path.join(branch_folder,group_table[0][i]+'.csv')
        data_reader = pd.read_csv(file_name_appended)
        counter = 0
        for j in range(1, number_of_groups+1):
            located_data = data_reader.iloc[counter:counter+group_table[j][i]] # Locate in the dataframe
            rows_to_write = located_data.values.tolist()
            counter += group_table[j][i]
            # writer_file = group_table[j][0]
            present_dir  =  os.getcwd()
            group_folder = os.path.join(present_dir,"Group_Wise_Folder")
            writer_file = os.path.join(group_folder,group_table[j][0])
            with open(writer_file, mode='a+', newline="") as file:
                stud_writer = csv.writer(file)
                stud_writer.writerows(rows_to_write)
    return












filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)