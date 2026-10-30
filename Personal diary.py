








import shutil
import os
import time
import sys


path = os.path.dirname(__file__) + os.sep

def wait(wait = 2):
    time.sleep(wait)

def clear():
    os.system("cls")

def get_width():
    return shutil.get_terminal_size().columns

def line():
    print("=" * get_width())


class Writing:
    def __init__(self, message):
        self.message = message

    def get_message(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} - {self.message}"

class File:
    def __init__(self, file):
        self.file = file

    def get_pathway(self):
        return path + self.file

class Write:
    def __init__(self, file, message):
        self.file = file
        self.message = message

    def write(self):
        with open(self.file, "a", encoding="utf-8") as file:
            file.write(f"{self.message}")
class Read:
    def __init__(self, file):
        self.file = file
        
    def read(self):
        with open(self.file, "r", encoding="utf-8") as file:
            content = file.readlines()
            for line in content:
                print(line.center(get_width()) + "\n")


def tablo():
    line()
    print("")
    print("Личный дневник 1.0 =)".center(get_width()))
    print("")
    line()
    print("")
    print("Options: 0 - quit; 1 - write a new chapter; 2 - read all chapters you have written".center(get_width()))
    print("")
    line()
    

def game():
    tablo()
    file = File("Diary.txt")
    option = int(input("Enter a index of option(0/1/2): ".center(get_width()).rstrip() + " "))
    while option > 2 or option < 0:
        option = int(input("Enter a index of option(0/1/2): ".center(get_width()).rstrip() + " "))
    match option:
        case 0:
            sys.exit()
        case 1:
            clear()
            tablo()
            message = Writing(input("Write a chapter: ".center(get_width()).rstrip() + " "))
            chapter = Write(file.get_pathway(), message.get_message())
            chapter.write()
            print("Chapter saved succesfully!".center(get_width()))
            line()
            wait(5)
            clear()
            game()
        case 2:
            clear()
            tablo()
            diary = Read(file.get_pathway())
            print("Here is your diary filled with your memories!".center(get_width()))
            diary.read()
            line()
            wait(5)
            input("Click enter when you want to continue!".center(get_width()).rstrip() + " ")
            clear()
            game()

game()
            
            
            
            
        
    

           
        

        
    
