
import os
import numpy as np

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
right_answer = answer_key.split(",")

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
            score_list = []
            
            for rowno, answer in enumerate(exam):
                if (len(answer) != 26):
                    writefile.writelines(
                        f"\nInvalid line of data: does not contain exactly 26 values:\n{exams[rowno]}\n")
                elif (len(answer[0]) != 9) or (answer[0][0] != "N") \
                    or ((answer[0][1:10]).isnumeric() == False):
                    writefile.writelines(f"\nInvalid line of data: N# is invalid\n{exams[rowno]}\n")
                else:
                    for i in range(25):
                        if answer[i+1] == right_answer[i]:
                            answer[i+1] = 4
                        elif answer[i+1] == "":
                            answer[i+1] = 0
                        else:
                            answer[i+1] = -1
                    score_list.append(answer)
            score_array = np.array(score_list,np.newaxis)
    return score_array     

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


    