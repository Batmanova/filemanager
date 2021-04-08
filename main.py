import platform
import os
import shutil
import send2trash

def listDirectories():
    listdir = os.listdir(os.getcwd()) #listdir - список всех файлов и папок, getcwd - текущий каталог
    for x in listdir:
        print(x)

def open():
    while True:
        listDirectories()
        if platform.system() == "Windows":
            print('\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            res = input('\nChoose a file/folder: ')
        else:
            res = input("Type folder path or command: ")

        if res == 'exit':
            break
        elif res == 'back':
            os.chdir('..')
        elif platform.system() == "Linux" or res in os.listdir(os.getcwd()):
            if os.path.isfile(res):
                if platform.system() == "Linux":
                    os.system('cat ' + res)
                else:
                    os.system('"' + res + '"')
            else:
                if platform.system() == "Linux":
                    os.popen('cd ' + res)
                os.chdir(res)
        else:
            print('Not exist')

def rename():
    if platform.system() == "Windows":
        while True:
            listDirectories()
            print('\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            print('Type "rename" to rename this directory')
            res = input('\nChoose a file to rename: ')
            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    new_name = input("Enter a new name: ")
                    ogDir = res
                    newDir = os.getcwd() + '\\' + new_name
                    shutil.move(ogDir, newDir)
                else:
                    os.chdir(res)
            elif res == 'exit':
                break
            elif res == 'back':
                os.chdir('..')
            elif res == 'rename':
                new_name = input("New name: ")
                ogDir = os.getcwd()
                os.chdir('..')
                newDir = os.getcwd() + '\\' + new_name
                shutil.move(ogDir, newDir)
            else:
                print('Not exist')
    else:
        while True:
            print('Type "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            res = input("Type file path: ")
            if os.path.isdir(res):
                os.popen('cd ' + res)
                listDirectories()
                res2 = input("Type filename: ")
                if os.path.isfile(res2):
                    res3 = input("New name: ")
                    os.system('mv ' + res2 + " " + res3)
                    listDirectories()
            elif res == "exit":
                break
            elif res == 'back':
                os.chdir('..')
            else:
                print('Not exist')

def copy(move):
    if platform.system() == "Windows":
        while True:
            listDirectories()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            print('Type "copy" to copy this directory')
            res = input('\nChoose a file to copy: ')
            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("Move " + res)
                    while True:
                        for x in range(len(drives)):
                            print(drives[x])
                        inp2 = input("\nChoose: ")
                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Enter a correct drive name.\n')
                    while True:
                        listDirectories()
                        print('Type "paste" to copy this file in current directory')
                        res2 = input('\nChoose: ')
                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")
                            else:
                                os.chdir(res2)
                        elif res2 == 'paste':
                            shutil.copy(og_path, os.getcwd())
                            break
                else:
                    os.chdir(res)
            elif res == 'exit':
                break
            elif res == 'back':
                os.chdir('..')
            elif res == 'copy':
                og_path = os.getcwd()
                print("Copying the current directory")
                while True:
                    for x in range(len(drives)):
                        print(drives[x])
                    inp2 = input("\nChoose: ")
                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Incorrect input\n')
                while True:
                    listDirectories()
                    print('\nType "paste" to copy this file in current directory')
                    res2 = input('\nChoose a folder: ')
                    print('\n')
                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")
                        else:
                            os.chdir(res2)
                    elif res2 == 'paste':
                        print(og_path)
                        folder_name = og_path.split('\\')[-1]
                        folder_directory = os.getcwd() + '\\' + folder_name
                        shutil.copytree(og_path, folder_directory)
                        break
            else:
                print('Not exist')
            if move:
                send2trash.send2trash(og_path)
    else:
        while True:
            res = input("Type file path: ")
            if os.path.isdir(res):
                os.chdir(res)
                need_file = input("Type filename: ")
                if os.path.isfile(need_file):
                    copy_dir = input("Type path to copy: ")
                    if os.path.isdir(copy_dir):
                        os.system('cp ' + need_file + " " + copy_dir)
                        listDirectories()
            elif res == "exit":
                break
            elif res == 'back':
                os.chdir('..')
            else:
                print("Incorrect dir input")
            if move:
                os.system('rm ' + res + '/' + need_file)

def delete():
    while True:
        listDirectories()
        print('\nType "exit" to exit from file manager.')
        print('Type "back" to go up one directory.')
        if platform.system() == "Windows":
            print('Type "delete" to delete directory')
            res = input('\nChoose a file to delete: ')
        else:
            res = input("Type file path: ")
        if res in os.listdir(os.getcwd()) and platform.system() == "Windows":
            if os.path.isfile(res):
                ans = input('Are you sure you want to delete folder? (YES/NO) ')
                if ans.lower() == 'yes' or 'y':
                    send2trash.send2trash(res)
            else:
                os.chdir(res)
        elif os.path.isfile(res) and platform.system() == "Linux":
            os.system('rm ' + res)
        elif res == 'exit':
            break
        elif res == 'back':
            os.chdir('..')
        elif res == 'delete':
            ans = input('Are you sure you want to delete folder? (YES/NO) ')
            if ans.lower() == 'yes' or 'y':
                path = os.getcwd()
                os.chdir('..')
                send2trash.send2trash(path)
        else:
            print('Not exist or not a file')

def create_windows():
    while True:
        listDirectories()
        print('\nType "exit" to exit from file manager.')
        print('Type "back" to go up one directory.')
        res = input('\nChoose a folder or create now: ')
        if res in os.listdir(os.getcwd()):
            os.chdir(res)
            check_create = input("If you want to create file, write down filename: ")
            if check_create == "exit":
                break
            else:
                os.system("copy nul " + check_create)
        elif res == 'exit':
            break
        elif res == 'back':
            os.chdir('..')
        elif res == "now":
            check_create = input("If you want to create file, write down filename: ")
            if check_create == "exit":
                break
            else:
                os.system("copy nul " + check_create + " > nul")
        else:
            print('No folder exist of this name.')

def create_linux():
    while True:
        res = input("Type file path: ")
        if os.path.isdir(res):
            os.popen('cd ' + res)
            os.chdir(res)
            file_or_dir = input("You want to create dir or file? ")
            if file_or_dir == 'file':
                name_input = input("Type filename: ")
                os.system('touch ' + name_input)
            if file_or_dir == 'dir':
                name_input = input("Type dirname: ")
                os.system('mkdir ' + name_input)
                listDirectories()
        elif res == "exit":
            break
        else:
            print("Incorrect file path")

def write():
    while True:
        res = input("Type file path: ")
        if os.path.isfile(res):
            write_res = input("Type text: ")
            os.system('echo ' + '"' + write_res + '" ' + '>> ' + res)
        elif res == "exit":
            break
        else:
            print("File not found")

list_of_commands = ["1", "2", "3", "4", "5", "6", "exit"]
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')] #от 65 до 90 чтоб отображал только диски
#проверяем тип системы
while True:
    if not (platform.system() == "Windows" or platform.system() == "Linux"):
        print("Unknown file system")
        break
    print("1.Open folder\n2.Rename\n3.Move and Paste\n4.Copy and Paste\n5.Delete\n6.Create\n7.Write into file\nexit")
    result = input("Choose: ")
    if platform.system() == "Windows":
        print('Drives: ')
        for i in range(len(drives)):
            print(drives[i])
        while True:
            inp = input("\nEnter your Choice: ")
            if inp in drives:
                os.chdir(inp + '\\')  # переходим в нужную папку
                break
            else:
                print('Incorrect input\n')
    if result == '1':
        open()
    if result == '2':
        rename()
    if result == '4':
        copy(False)
    if result == '3':
        copy(True)
    if result == '5':
       delete()
    if result == '6':
        if platform.system() == "Windows":
            create_windows()
        else:
            create_linux()
    if result == '7':
        if platform.system() == "Windows":
            print("You can't write into file in console. Please open file to write in it")
        else:
            write()
    if result == "exit":
        break
    if not (result in list_of_commands):
        print("Wrong input")
