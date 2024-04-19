
import os
import numpy as np

def checkfile(reportFile):
    if os.path.isfile(reportFile) == 1:
        with open(reportFile, "a+") as writefile:
            writefile.writelines("\n\n>>> =========================== RESTART " + \
                                 "===========================\n" + ">>>\n")

def report(classFile,reportFile,name):
    checkfile(reportFile)
    with open(classFile, "r") as readfile:
        with open(reportFile, "a+") as writefile:
            writefile.writelines(
                "Enter a class to grade (i.e. class1 for class1.txt): " + name + \
                    "\nSuccessfully opened " + name + ".txt" + \
                        "\n\n*** ANALYZING ***\n")
            readfile.seek(0)
            exams = [line.rstrip('\n') for line in readfile]
            exam = [line.split(",") for line in exams]
            for i, answer in enumerate(exam):
                if (len(answer) != 26):
                    writefile.writelines(
                        f"\nInvalid line of data: does not contain exactly 26 values:\n{exams[i]}\n")

current_path = os.getcwd()
datapath = os.path.join(current_path, "Data")
name = input("Enter a class to grade (i.e. class1 for class1.txt): ")
filename = name + ".txt"
filepath = os.path.join(datapath,filename)

try:
    reportFile = "task2.txt"
    classFile = filepath
    report(classFile,reportFile,name)
    
except (KeyboardInterrupt, EOFError):
    print("Keyboard interrupt!")

except OSError:
    print("File not found.")


    