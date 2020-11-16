import os
import re
os.system('cls' if os.name == 'nt' else 'clear')
def rename_FIR(folder_name):
    pass


    

def rename_Game_of_Thrones(folder_name):
    # rename Logic 
    os.chdir(folder_name)
    files = os.listdir(folder_name)
    for file_got in files:
        series_info = re.split('-', file_got)
        series_name, given_number, episode_name_given = series_info[0], series_info[1], series_info[2]
        series_name = series_name.strip()
        given_number = given_number.strip()
        episode_name_given = episode_name_given.strip()
        series_info = re.split('x', given_number)
        season_number, episode_number = series_info[0], series_info[1]
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        if len(season_number) < season_padding:
            season_number = int(int(season_padding) -
                                len(season_number))*'0'+season_number
        if len(episode_number) < episode_padding:
            episode_number = int(int(episode_padding) -
                                 len(episode_number))*'0'+episode_number
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        new_name = series_name + ' - Season ' + \
            season_number + ' Episode '+episode_number + ' - '
        series_info = re.split('\.', episode_name_given)
        episode_name = series_info[0]
        series_info = re.split('\.', file_got)
        extension = series_info[-1]
        new_name += episode_name + '.' + extension.strip()
        os.rename(file_got, new_name)


    

def rename_Sherlock(folder_name):
    # rename Logic 
    pass



    

def rename_Suits(folder_name):
    # rename Logic 
    pass


    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic 
    pass



# Preprocessing for getting the folder name and to get the  padding of episode and padding of the season
#Current PAth
current_path = os.getcwd()
folder_path = os.path.join(current_path, 'Subtitles')
season_padding = 0
episode_padding = 0
flag=True
nameOfSeries = {1:'FIR',2:'Game of Thrones',3:'Sherlock',4:'Suits',5:'How I Met Your Mother'}
while flag:
    webSeriesIndex= int(input(f"Enter the title of WebSeries, Available titles is \n{nameOfSeries}\n"))
    if(webSeriesIndex in nameOfSeries):
        flag_season_padding = True
        while flag_season_padding:
            season_padding = input("Please enter padding for season number: ")
            try:
                season_padding = float(season_padding)
                flag_season_padding = False #Valid Padding Found
            except:
                print('Season padding is not valid Some Error Occured\n')
        flag_episode_padding = True
        while flag_episode_padding:
            episode_padding = input("Please enter padding for Episode number: ")
            try:
                episode_padding = float(episode_padding)
                flag_episode_padding = False #Valid Padding Found
            except:
                print('Season padding is not valid Please enter again\n')
        flag=False
        concernedPath = os.path.join(folder_path,nameOfSeries[webSeriesIndex])
        if webSeriesIndex ==1:
            duplicate_file = rename_FIR(concernedPath)
            print(f"Total Duplicate files removed -> {duplicate_file}")
        elif webSeriesIndex ==2:
            rename_Game_of_Thrones(concernedPath)
        elif webSeriesIndex ==3:
            rename_Sherlock(concernedPath)
        elif webSeriesIndex ==4:
            duplicate_file = rename_Suits(concernedPath)
            print(f"Total Duplicate files removed -> {duplicate_file}")
        else:
            duplicate_file = rename_How_I_Met_Your_Mother(concernedPath)
            print(f"Total Duplicate files removed -> {duplicate_file}")
            


    else:
        print("Series is not in the Database of the existing series please select from the database:)")


