import os
import shutil
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.txt', '.docx', '.doc', '.xls'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
}
location=input("enter folder location")
file_list=os.listdir(location)#fetch all the file names from the pathh
for file in file_list:
    og_file=os.path.join(location,file)#combine the path and the original file name 
    file_ext=os.path.splitext(file)[1].lower()
    moved=False
    for category,extensions in file_types.items():
        if file_ext in extensions:
            folder_path=os.path.join(location,category)
            os.makedirs(folder_path, exist_ok=True)#create a new folder with the new path 
            shutil.move(og_file,os.path.join(folder_path,file))#shift file to the new folder path 
            print("Moved: ",file," to ",folder_path)
            moved=True
            break
    if moved==False: #in case there is a new file type 
        new_folder=os.path.join(location,"Others")
        os.makedirs(folder_path,exist_ok=True)
        shutil.move(og_file,os.path.join(new_folder,file))
        print("Moved :",file, "to ",new_folder)

print("Process Excecuted")

