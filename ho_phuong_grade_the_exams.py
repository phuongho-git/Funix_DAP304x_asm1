

import os
import numpy as np

# đáp án của bài thi
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
right_answer = answer_key.split(",")

# function xác định các dòng hợp lệ và tính điểm từng câu trả lời
def report(classFile,reportFile,name):
    with open(classFile,"r") as readfile:
        with open(reportFile,"a+") as writefile:

            writefile.write("Enter a class to grade (i.e. class1 for class1.txt): " + name)
            writefile.write("\nSuccessfully opened " + name + ".txt")
            writefile.write("\n\n*** ANALYZING ***\n")    

            readfile.seek(0)
            exams = readfile.readlines()
            row_count = len(exams) # tổng số dòng trong file    
            check_list = [] # list trống để chứa điểm từng câu trả lời
            score_lines = [] # list trống để chứa tổng điểm của bài thi

            for rowno in range(row_count):
                exam = exams[rowno].strip() # cắt từng dòng
                answers = exam.split(",") # tách riêng thành phần từng dòng
                id = answers[0] # lấy id của học sinh trong lớp                
           
                # in các dòng không chứa 26 giá trị
                if (len(answers) != 26):
                    writefile.write("\nInvalid line of data: does not contain exactly 26 values:\n")
                    writefile.write(exam)
                    writefile.write("\n")

                # in các dòng có N# không hợp lê
                elif (len(id) != 9 
                    or id[0] != "N"
                    or id[1:10].isnumeric() == False):
               
                    writefile.write("\nInvalid line of data: N# is invalid\n")
                    writefile.write(exam)
                    writefile.write("\n")

                # tính điểm từng câu trả lời cho các dòng hợp lệ
                else:
                    total_score = 0 # biến tính tổng điểm cho từng học sinh
                    answers.pop(0) # bỏ id học sinh
                    # list trống sẽ chứa điểm cho câu trả lời của từng học sinh
                    check_answer = []                       

                    for answer in range(25):
                        if answers[answer] == right_answer[answer]:
                            score = 4
                            total_score += score
                            check_answer.append(4)                               

                        elif answers[answer] == "":
                            score = 0
                            total_score += score
                            check_answer.append(0)                                

                        else:
                            score = -1
                            total_score += score
                            check_answer.append(-1)

                    score_lines.append(total_score)                                                                                    
                    check_list.append(check_answer)              
                                                                                                               
            # tạo biến toàn cục chứa điểm của mỗi câu hỏi và tổng điểm của từng học sinh
            global check_array
            global score_array
            global valid_rows
            check_array = np.array(check_list)            
            score_array = np.array(score_lines)
            valid_rows = len(check_array)

            # ghi thông báo nếu các dòng đều hợp lệ                     
            if valid_rows == row_count:
                writefile.write("\nNo errors found!\n")

            writefile.write("\n*** REPORT ***\n")
            # ghi tổng số dòng 
            writefile.write("\nTotal lines of data:" + \
                            str(row_count))
            # ghi tổng số dòng hợp lệ
            writefile.write("\nTotal valid lines of data:" + \
                            str(valid_rows))
            # ghi tổng số dòng không hợp lệ   
            writefile.write("\nTotal invalid lines of data:" + \
                            str(row_count - valid_rows) + "\n") 

def checkfile(taskFile):
    # check file có tồn tại không
    if os.path.isfile(taskFile) == 1:
    # nếu file tồn tại thì viết thông báo restart
        with open(taskFile, "a+") as writefile:
            writefile.writelines("\n\n>>> ================================ RESTART " + \
                                 "================================\n" + ">>>\n")         
   
                                                 
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
    # check file task 2 có tồn tại không
    taskFile ="task2.txt"
    checkfile(taskFile)

    # gán biến cho function report
    classFile = filepath
    reportFile = "task2.txt"

    # task 2: ghi file thông báo tổng số dòng, số dòng hợp lệ, không hợp lệ
    # ghi chi tiết giá trị của các dòng không hợp lệ
    report(classFile,reportFile,name)

    # hiện thông báo mở file thành công ra màn hình
    print("Successfully opened " + filename)
    print("Analyzing...")

    # check file task 3 có tồn tại không
    taskFile = "task3.txt"
    checkfile(taskFile)

    # task 3: ghi file khác chứa các thông báo như task 2 và tính các giá trị thống kê
    with open(classFile, "r") as readfile:
        with open("task3.txt", "a+") as writefile:

            # ghi lại các thông báo như task 2
            report(classFile,"task3.txt",name)

            # thống kê số học sinh đạt điểm cao (> 80)
            high_score = 0
            for i in range(valid_rows):
                if int(score_array[i]) > 80:
                    high_score += 1
            writefile.write("\nNumber of students achieving high scores : " + \
                            str(high_score))
    
            # thống kê điểm trung bình của học sinh trong lớp
            writefile.write("\nMean (average) score: " + str(round(score_array.mean(),2)))

            # thống kê điểm cao nhất trong lớp
            writefile.write("\nHighest score: " + str(score_array.max()))

            # thống kê điểm thấp nhất trong lớp
            writefile.write("\nLowest score: " + str(score_array.min()))

            # thống kê miền giá trị của điểm trong lớp
            writefile.write("\nRange of scores: " + str(score_array.max() - score_array.min()))

            # thống kê giá trị trung vị của điểm trong lớp
            writefile.write("\nMedian score: " + str(round(np.median(score_array))))


            # thống kê các câu hỏi bị bỏ qua nhiều nhất
            # lấy list các câu trả lời có giá trị = 0 (0 điểm cho mỗi câu bị bỏ qua)
            null_count = np.count_nonzero(check_array == 0, axis = 0)
            # lấy số thứ tự (index) của các câu trả lời bị bỏ qua
            null_number = np.argwhere(null_count == null_count.max())
            # tính tỉ lệ học sinh bỏ qua câu hỏi
            null_ratio = round((null_count.max() / valid_rows * 100), 2)         
            # ghi số thứ tự - số học sinh bỏ qua - tỉ lệ bỏ qua của câu hỏi đó
            writefile.write("\nMost skipped answers to the question: " + \
                            str(null_number[:,0]) + " - " + \
                            str(null_count.max()) + " skips - " + \
                            str(null_ratio) + "%")
            

            # thống kê các câu hỏi bị trả lời sai nhiều nhất
            # lấy list các câu trả lời có giá trị = -1 (-1 điểm cho mỗi câu trả lời bị sai)
            bad_count = np.count_nonzero(check_array == -1, axis=0)
            # lấy số thứ tự (index) của các câu trả lời sai
            bad_number = np.argwhere(bad_count == bad_count.max())
            # tính tỉ lệ học sinh trả lời sai
            bad_ratio = round((bad_count.max()/valid_rows *100), 2)
            # ghi số thứ tự - số học sinh trả lời sai - tỉ lệ trả lời sai của câu hỏi đó
            writefile.write("\nMost incorrect answers to the question: " + \
                            str(bad_number[:,0]) + " - " + \
                            str(bad_count.max()) + " wrong turns - " + \
                            str(bad_ratio) + "%\n")
                            

    # task 4: tạo một tệp “kết quả” chứa tổng điểm cho từng học sinh
    with open(classFile, "r") as readfile:
        with open(f"{name}_grades.txt", "w") as writefile:
            readfile.seek(0)
            exams = readfile.readlines()
            row_count = len(exams) # tổng số dòng trong file
            valid_id = [] # list trống sẽ chứa id của bài thi hợp lệ

            for rowno in range(row_count):
                exam = exams[rowno].strip() # cắt từng dòng
                answers = exam.split(",") # tách riêng thành phần từng dòng
                id = answers[0] # lấy id của học sinh trong lớp

                # lấy id của bài thi hợp lệ
                if (len(answers) == 26) & ((len(id) == 9) & (id[0] == "N") & \
                                           (id[1:10].isnumeric() == True)):
                    valid_id.append(id)

            # ghi file tính điểm cho từng học sinh trong lớp
            for line in range(valid_rows):
                student_score = valid_id[line] + "," + str(score_array[line])
                writefile.writelines(student_score + "\n")

    print("Successfully created " + f"{name}_grades.txt")

except (KeyboardInterrupt, EOFError):
    print("Keyboard interrupt!")

except OSError:
    print("File not found.")

except Exception:
    print("Something went wrong!")