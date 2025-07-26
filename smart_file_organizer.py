import os
import shutil
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.txt', '.docx', '.doc', '.xls'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
}
location=input("enter folder location")
file_list=os.listdir(location)
for file in file_list:
    og_file=os.path.join(location,file)
    file_ext=os.path.splitext(file)[1].lower()
    moved=False
    for category,extensions in file_types.items():
        if file_ext in extensions:
            folder_path=os.path.join(location,category)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(og_file,os.path.join(folder_path,file))
            print("Moved: ",file," to ",folder_path)
            moved=True
            break
    if moved==False:
        new_folder=os.path.join(location,"Others")
        os.makedirs(folder_path,exist_ok=True)
        shutil.move(og_file,os.path.join(folder_path,file))
        print("Moved :",file, "to ",new_folder)

print("Process Excecuted")

