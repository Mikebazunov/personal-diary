








import shutil
import os
import time
import sys

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
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
        return timestamp + self.message

class File:
    def __init__(self, file):
        self.file = file

    def get_pathway(self):
        return path + self.file

class Actions:
    def __init__(self, file, message):
        self.file = file
        self.message = message

    def read(self):
        with open(self.file, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)

    def write(self):
        with open(self.file, "a", encoding="utf-8") as file:
            file.write(self.message)

           
        

        
    
