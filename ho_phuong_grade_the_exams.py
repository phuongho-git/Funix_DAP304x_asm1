
import os
import numpy as np

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
def report(classFile,task2File,name):
    checkfile(task2File)
    with open(classFile, "r") as readfile:
        with open(task2File, "a+") as writefile:
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
                
                # tính điểm từng câu trả lời cho các dòng hợp lệ
                else:
                    for i in range(25):
                        if answer[i+1] == right_answer[i]:
                            answer[i+1] = 4
                        elif answer[i+1] == "":
                            answer[i+1] = 0
                        else:
                            answer[i+1] = -1
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
                
    return np.array(score_list) # trả về mảng numpy chứa điểm của mỗi câu trả lời cho từng học sinh

# task 4: function ghi tổng số điểm của từng học sinh
def score_count(classFile,task4File,name):
    score_N = report(classFile,task4File,name) # chạy function lấy mảng chứa điểm của mỗi câu trả lời
    score_array = (np.array(score_N,np.newaxis)[:, 1:26]).astype(int) # bỏ N# chỉ lấy điểm số
    student_score = np.sum(score_array, axis = 1) # tính tổng điểm của từng học sinh
    
    # ghi file điểm cho lớp học với N# và tổng điểm của từng học sinh
    with open(f"{name}_grades.txt", "w") as writefile:
        for i in range(len(score_N)):
            writefile.write(f"{score_N[i,0]},{student_score[i]}\n")
    return score_array # trả về mảng numpy bỏ N# chỉ chứa điểm của từng học sinh

# task 3: function tính các giá trị thống kê của điểm số các học sinh trong lớp
def report_analysis(classFile,task3File,name):
    score_array = score_count(classFile,task3File,name) # lấy mảng numpy bỏ N# chỉ chứa điểm
    student_score = np.sum(score_array, axis = 1) # tính tổng điểm của từng học sinh 
    
    with open(task3File, "a+") as writefile:
        
        # thống kê số học sinh đạt điểm cao (> 80)
        writefile.write(f"\nNumber of students achieving high scores: {sum(student_score > 80)}")
        
        # thống kê điểm trung bình của học sinh trong lớp
        writefile.write(f"\nMean (average) score: {round(student_score.mean(),2)}")
        
        # thống kê điểm cao nhất trong lớp
        writefile.write(f"\nHighest score: {student_score.max()}")
        
        # thống kê điểm thấp nhất trong lớp
        writefile.write(f"\nLowest score: {student_score.min()}")
        
        # thống kê miền giá trị của điểm trong lớp
        writefile.write(f"\nRange of score: {student_score.ptp()}")
        
        # thống kê giá trị trung vị của điểm trong lớp
        writefile.write(f"\nMedian score: {np.median(student_score).astype(int)}")
            
        # thống kê các câu bị bỏ qua nhiều nhất
        # là các câu trả lời có giá trị = 0 (0 điểm cho mỗi câu bị bỏ qua)
        # tạo mảng chứa tổng số lượt bỏ qua cho mỗi câu
        null_count = np.sum(score_array == 0, axis = 0)
        # lấy index của các câu bị bỏ qua nhiều nhất
        null_number = np.argwhere(null_count == null_count.max())
        # lấy số thứ tự (index +1) của các câu bị bỏ qua nhiều nhất
        # đổi thành string
        null_str = ""
        for i, val in enumerate(null_number):
            null = val[0] + 1
            null_str = null_str+ f"{null}-"            
        # tính tỉ lệ học sinh bỏ qua câu hỏi
        null_ratio = round((null_count.max() / len(score_array) * 100), 2)
        # ghi số thứ tự - số học sinh bỏ qua - tỉ lệ bỏ qua của câu hỏi đó
        writefile.write(
            "\nMost skipped answers to the question: " + null_str +\
                f" {null_count.max()} skips- {null_ratio} %")
            
        # thống kê các câu hỏi bị trả lời sai nhiều nhất
        # là các câu trả lời có giá trị = -1 (-1 điểm cho mỗi câu trả lời bị sai)
        # tạo mảng chứa tổng số lượt sai cho mỗi câu hỏi
        bad_count = np.sum(score_array == -1, axis = 0)
        # lấy index của các câu trả lời sai
        bad_number = np.argwhere(bad_count == bad_count.max())
        # lấy số thứ tự (index +1) của các câu trả lời sai
        # đổi thành string
        bad_str = ""
        for i, val in enumerate(bad_number):
            bad = val[0] + 1
            bad_str = bad_str+ f"{bad}-"
        # tính tỉ lệ học sinh trả lời sai   
        bad_ratio = round((bad_count.max() / len(score_array) * 100), 2)
        # ghi số thứ tự - số học sinh trả lời sai - tỉ lệ trả lời sai của câu hỏi đó
        writefile.write(
            "\nMost incorrect answers to the question: " + bad_str +\
                f" {bad_count.max()} wrong turns- {bad_ratio} %\n")                                                    
    
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
    task2File = "task2.txt"
    classFile = filepath
    report(classFile,task2File,name)
    
    # hiện thông báo mở file thành công ra màn hình
    print("Successfully opened " + filename)
    print("Analyzing...")
    
    # gán biến và chạy function task 4
    task3File = "task3.txt"
    report_analysis(classFile,task3File,name)

    # hiện thông báo tạo file tính điểm từng học sinh
    print(f"Successfully created {name}_grades.txt")
    
# catch ngoại lệ khi nhập bàn phím
except (KeyboardInterrupt, EOFError):
    print("Keyboard interrupt!")

# catch tất cả các ngoại lệ về sai tên file, đường dẫn, lưu trữ
except OSError:
    print("File not found.")

# catch tất cả các ngoại lệ khác
except Exception:
    print("Something went wrong!")   