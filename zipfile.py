
#this is where my modules will be imported
import os
from os.path import exists
import shutil
import sys
import time
import zipfile
from zipfile import ZipFile
from pathlib import Path  
from shutil import copyfile


# These are my functions for each option
def zipchecker():

  global Valid_zipfile
  global zipfile_validator

  if zipfile_validator == "True":
    print("")
    print("Zipfile is loaded and valid")
    return

  with open("transaction_folder/transaction.txt","a") as T:
    T.write("\nZipfile has been loaded")
  Valid_zipfile = input("Input zipfile here: ")
  zipfile_validator = "True"
#########################################
def file_contents(Valid_zipfile):
  if Valid_zipfile:
    with open("transaction_folder/transaction.txt","a") as T:
      T.write("\nFile contents displayed")
    with ZipFile(Valid_zipfile, "r") as zip_f:
        zip_f.printdir()
  else:
    print("Not avaliable to print no zipfile detected")
    with open("transaction_folder/transaction.txt","+a") as T:
      T.write("File contents nil")
####################################
def extraction(Valid_zipfile):
  if Valid_zipfile:
    with open("transaction_folder/transaction.txt","+a") as T:
      T.write("\nFile Has been extracted")
    with ZipFile(Valid_zipfile, "r") as zip_f:
        zip_f.extractall(directory_creation)
  else:
    print("Not avaliable to print no zipfile detected")
    with open("transaction_folder/transaction.txt","+a") as T:
      T.write("File contents nil")
#####################################
def file_details():
  print("")
  print("\tFile Path:", os.getcwd())
  print("\tFile Size:", file_statistic.st_size)
  print("\tFile Access:", file_statistic.st_atime)
  print("\tFile Creation:", file_statistic.st_ctime)
  #os.getcwd geeksforgeeks.org(2025)



#This is where the directory will be created to store the transaction file
directory_creation = "transaction_folder/"

directory = Path(directory_creation)

direct = directory.mkdir(parents=False, exist_ok=True)

file_statistic = directory.stat()
#These are used for function of zipchecking and allows for the file to load
Valid_zipfile  = None
zipfile_validator = False

#these variables are used to help create the transaction text file and move it into the folder
Transaction_file_creation = open("transaction.txt","x")

original_fp = "transaction.txt"

new_fp = "transaction_folder/transaction.txt"

Change_original = Path(original_fp)

Change_new = Path(new_fp)

shutil.move(Change_original, Change_new)

input_file_path = new_fp
#These are the display values
print("")
print("Program started", time.ctime())
print("")
time.sleep(2.5)
os.system('clear')

#This is the menu that will be displayed each time the code is run
def menu():
  print("Zipfile Program")
  print("")
  print("1. Load zip file")
  time.sleep(0.5)
  print("2. Zip file details")
  time.sleep(0.2)
  print("3. Zip file contents")
  time.sleep(0.2)
  print("4. Extract zip file")
  time.sleep(0.2)
  print("5. Quit")

#simple graphical loading function
def loading():
  print("x")
  time.sleep(0.4)
  os.system('clear')
  print("+")
  time.sleep(0.4)
  os.system('clear')
  print('x')
  time.sleep(0.4)
  os.system('clear')
  print("+")
  time.sleep(0.4)
  os.system('clear')




      
  



#this is the choice loop where you can choose the options between 1 to 5
while True:
  menu()
  
  Choice = int(input("\nChoose an option: "))
  
  if Choice == 1:
    zipchecker()
    print("file loaded returning to menu")
    time.sleep(1)
    os.system('clear')
    loading()
  elif Choice == 2:
    file_details()
    print("file details shown returning to menu")
    time.sleep(1)
    os.system('clear')
    loading()
  elif Choice == 3:
    file_contents(Valid_zipfile)
    print("file content shown returning to menu")
    time.sleep(1)
    os.system('clear')
    loading()
  elif Choice == 4:
    extraction(Valid_zipfile)
    print("file extracted returning to menu")
    time.sleep(1)
    os.system('clear')
    loading()
  elif Choice == 5:
    print("goodbye")
    break

#This is validaton for the choice option so it stays between the values
while True:
  try:
    Choice = int(Choice)
  except ValueError:
    print("")
    print("enter correct integer value")
    try:
      Choice = int(input("Input option here: "))
    except ValueError:
      continue
  if Choice < 6 and Choice > 0 :
    break
  else:
    print("")
    print("Enter between the range of 1 to 5")
    try:
      print("")
      Choice = int(input("Input option here: "))
    except ValueError:
      print("")
    continue