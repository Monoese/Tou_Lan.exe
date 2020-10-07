import os
import shutil
import sys
#C:/Users/Rya/AppData/Local/CCP/EVE/c_eve_sharedcache_tq_tranquility/settings_Default/Backup
user_confirmation = input("This script will clone the original pair of user&character profile files and replace other users'&characters' profile with them.\nMake sure that you are using default profile folder named \'Default\' as you profile folder name. Only profile files under \'Default\' folder will be edited\nReply \'y\' to continue: ")

if user_confirmation != "y":
    print("please check the correctness of your folder dir and profile files before continuing")
    sys.exit()
username = input("what is the windows username?: ")
path_0 = input("where are char & user setting DAT files?(PLZ use \'/\'): ")
path_1 = f'C:/Users/{username}/AppData/Local/CCP/EVE/c_eve_sharedcache_tq_tranquility/settings_Default'
path_2 = f'C:/Users/{username}/AppData/Local/CCP/EVE/c_eve_sharedcache_sisi_singularity/settings_Default'
char_0 = []
user_0 = []
char_1 = []
user_1 = []
char_2 = []
user_2 = []

if os.path.isdir(path_0) == True:
    files_0 = os.listdir(path_0)
    for file in files_0:
        if len(file) == 24:
            char_0.append(file)
        elif len(file) == 22:
            user_0.append(file)

if os.path.isdir(path_1) == True:
    files_1 = os.listdir(path_1)
    for file in files_1:
        if len(file) == 24:
            char_1.append(file)
        elif len(file) == 22:
            user_1.append(file)
    for user in user_1:
        shutil.copy(f'{path_0}/{user_0[0]}', f'{path_1}/{user}')
    for char in char_1:
        shutil.copy(f'{path_0}/{char_0[0]}', f'{path_1}/{char}')
    print('tranquility profile reset completed')
else:
    print("tranquility profile folder not detected. Proceeding to singularity profile!")

if os.path.isdir(path_2) == True:
    files_2 = os.listdir(path_1)
    for file in files_2:
        if len(file) == 24:
            char_2.append(file)
        elif len(file) == 22:
            user_2.append(file)
    for user in user_2:
        shutil.copy(f'{path_0}/{user_0[0]}',f'{path_2}/{user}')
    for char in char_2:
        shutil.copy(f'{path_0}/{char_0[0]}',f'{path_2}/{char}')
    print('singularity profile reset completed')
else:
    print("singularity profile folder not detected. Duplication finished!")
