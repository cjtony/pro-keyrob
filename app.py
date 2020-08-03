import os, getpass, sys, datetime
from pynput.keyboard import Listener
from io import open

user_pc = getpass.getuser()
directory_save_txt = os.listdir("C:/Users/marco")

for d in directory_save_txt:
    print("Usuario: {}, Archivo/Carpeta: {} ".format(user_pc, d))