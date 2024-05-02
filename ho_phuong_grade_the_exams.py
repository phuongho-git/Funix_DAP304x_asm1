import os

import pandas as pd

# Đáp án của bài thi.
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
right_answer = answer_key.split(",")


# check file có tồn tại không, nếu có thì viết thông báo RESTART.
def checkfile(reportFile):
    if os.path.isfile(reportFile) == 1:
        with open(reportFile, "a+") as writefile:
            writefile.writelines(
                "\n\n>>> =========================== RESTART "
                + "===========================\n"
                + ">>>\n"
            )


# task 2: function xác định các dòng không hợp lệ và tính điểm từng câu trả lời.
def report(classFile, reportFile, name):
    checkfile(reportFile)
    df = pd.read_csv(classFile, sep=",", header=None, on_bad_lines="skip")
    print(df)


# lấy đường dẫn của folder người dùng
current_path = os.getcwd()
# lấy đường dẫn của folder Data chứa file cần phân tích
datapath = os.path.join(current_path, "Data")
# nhập tên file từ người dùng
name = input("Enter a class to grade (i.e. class1 for class1.txt): ")
filename = name + ".txt"
# lấy tên file cần phân tích trong folder Data
filepath = os.path.join(datapath, filename)

# chạy code nếu không có ngoại lệ
try:
    # gán biến và chạy function task 2
    reportFile = "task2.txt"
    classFile = filepath
    report(classFile, reportFile, name)


# catch ngoại lệ khi nhập bàn phím
except (KeyboardInterrupt, EOFError):
    print("Keyboard interrupt!")

# catch tất cả các ngoại lệ về sai tên file, đường dẫn, lưu trữ
except OSError:
    print("File not found.")
