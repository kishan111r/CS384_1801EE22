import os
import re
os.system('cls' if os.name == 'nt' else 'clear')
def rename_FIR(folder_name):
    # rename Logic 
    pass


    

def rename_Game_of_Thrones(folder_name):
    # rename Logic 
    pass


    

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

    else:
        print("Series is not in the Database of the existing series please select from the database:)")


