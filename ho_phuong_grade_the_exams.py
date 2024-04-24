
import os
import csv
import numpy as np
import pandas as pd

# đáp án của bài thi
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
right_answer = answer_key.split(",")

# check file có tồn tại không, nếu có thì viết thông báo RESTART
def checkfile(reportFile):
    if os.path.isfile(reportFile) == 1:
        with open(reportFile, "a+") as writefile:
            writefile.writelines("\n\n>>> =========================== RESTART " + \
                                 "===========================\n" + ">>>\n")

# task 2: function xác định các dòng không hợp lệ và tính điểm từng câu trả lời
def report(classFile,reportFile,name):
    checkfile(reportFile)
    # task 2: function xác định các dòng không hợp lệ và tính điểm từng câu trả lời
def report(classFile,reportFile,name):
    checkfile(reportFile)
    with open(classFile, "r") as readfile:
        with open(reportFile, "a+") as writefile:
            writefile.writelines(
                "Enter a class to grade (i.e. class1 for class1.txt): " + name + \
                    "\nSuccessfully opened " + name + ".txt" + \
                        "\n\n*** ANALYZING ***\n")
            readfile.seek(0)
            exams = [line.rstrip('\n') for line in readfile] # cắt từng dòng
            exam = [line.split(",") for line in exams] # tách riêng thành phần trong dòng
            score_list = [] # list trống để chứa tổng điểm của bài thi
            
            for rowno, answer in enumerate(exam):
                # in các dòng không chứa 26 giá trị
                if (len(answer) != 26):
                    writefile.writelines(
                        f"\nInvalid line of data: does not contain exactly 26 values:\n{exams[rowno]}\n")
                    
                # in các dòng có N# không hợp lê
                elif (len(answer[0]) != 9) or (answer[0][0] != "N") \
                    or ((answer[0][1:10]).isnumeric() == False):
                    writefile.writelines(f"\nInvalid line of data: N# is invalid\n{exams[rowno]}\n")
                    
                else:
                    score_list.append(answer)
            
            # ghi thông báo nếu các dòng đều hợp lê
            if len(score_list) == len(exams):
                writefile.write("\nNo errors found!\n")
                
            writefile.write("\n*** REPORT ***\n")
            # ghi tổng số dòng 
            writefile.write(f"\nTotal lines of data: {len(exams)}")
            # ghi tổng số dòng hợp lệ
            writefile.write(f"\nTotal valid lines of data: {len(score_list)}")
            # ghi tổng số dòng không hợp lệ   
            writefile.write(f"\nTotal invalid lines of data: {len(exams)-len(score_list)}")
        
    # trả về dataframe chứa điểm của mỗi câu trả lời cho từng học sinh
    return pd.DataFrame(score_list).set_index(0)
   

# lấy đường dẫn của folder người dùng
current_path = os.getcwd()
# lấy đường dẫn của folder Data chứa file cần phân tích
datapath = os.path.join(current_path, "Data")
# nhập tên file từ người dùng
name = input("Enter a class to grade (i.e. class1 for class1.txt): ")
filename = name + ".txt"
# lấy tên file cần phân tích trong folder Data
filepath = os.path.join(datapath,filename)

# chạy code nếu không có ngoại lệ
try:
    # gán biến và chạy function task 2
    reportFile = "task2.txt"
    classFile = filepath
    report(classFile,reportFile,name)
    
    
# catch ngoại lệ khi nhập bàn phím
except (KeyboardInterrupt, EOFError):
    print("Keyboard interrupt!")

# catch tất cả các ngoại lệ về sai tên file, đường dẫn, lưu trữ
except OSError:
    print("File not found.")