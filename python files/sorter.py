import os, shutil

path = r"C:/Users/Dell/OneDrive/Desktop/Automatic/"

file_name = os.listdir(path)

folder_names = ['pdf files', 'image files', 'python files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):

        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".py" in file and not os.path.exists(path + "python files/" + file):
         shutil.move(path + file, path + "python files/" + file)