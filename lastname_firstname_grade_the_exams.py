
""" # nhập tên file
filename = input("Enter a filename: ")

# test ngoại lệ khi nhập tên file

try:
    

if filename == "class1":
    
    with open("./Data/class1.txt", "r") as file1:
        print(file1.readline())

elif filename == "class2":
    
    with open("./Data/class2.txt", "r") as file2:
        print(file2.readline())

else:

    print ("Sorry, I can't find this filename.") """

import numpy as np

# đáp án của bài thi
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
right_answer = answer_key.split(",")


def report(classFile,reportFile):
    with open(classFile,"r") as readfile:
        with open(reportFile,"a+") as writefile:    

            exams = readfile.readlines()
            row_count = len(exams)      
            check_list = []
            score_lines = []

            with open("task4.txt","w") as task4:

                for rowno in range(row_count):
                    exam = exams[rowno].strip()
                    answers = exam.split(",")
                    id = answers[0]                   
           

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

                    # tạo list các dòng hợp lệ
                    else:                                                                              
                        total_score = 0
                        answers.pop(0)
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
                                check_answer.append(-1)

                        score_lines.append(total_score)                                                                                    
                        check_list.append(check_answer)

                        #in kết quả của mỗi học sinh
                        task4.write(id + "," + str(total_score) + "\n")                 
                                                                                                               
            # tạo biến chứa điểm của mỗi câu hỏi
            global check_array
            global score_array
            global valid_rows
            check_array = np.array(check_list)            
            score_array = np.array(score_lines)
            valid_rows = len(check_array)

             
            # in thông báo nếu các dòng đều hợp lệ                     
            if valid_rows == row_count:
                writefile.write("\n\nNo errors found!")

            # ghi file report
            writefile.write("\n\n*** REPORT ***\n")
            # in tổng số dòng 
            writefile.write("\nTotal lines of data:" + \
                        str(row_count))
            # tổng số dòng hợp lệ
            writefile.write("\nTotal valid lines of data:" + \
                        str(valid_rows))
            # tổng số dòng không hợp lệ   
            writefile.write("\nTotal invalid lines of data:" + \
                        str(row_count - valid_rows))     
                                                 

classFile = "./Data/class5.txt"
reportFile = "task2.txt"
report(classFile,reportFile)

with open("task3.txt","+a") as task3:
    classFile = "./Data/class5.txt"
    reportFile = "task3.txt"
    report(classFile,reportFile)

    high_score = 0
    for i in range(valid_rows):
        if int(score_array[i] > 80):
            high_score += 1
    task3.write("\n\nNumber of students achieving high scores:" + \
                str(high_score))
    
    task3.write("\nMean (average) score:" + str(round(score_array.mean(),2)))

    task3.write("\nHighest score:" + str(score_array.max()))

    task3.write("\nLowest score:" + str(score_array.min()))

    task3.write("\nRange of scores:" + str(score_array.max() - score_array.min()))

    task3.write("\nMedian score:" + str((np.median(score_array))*10/10))

    null_count = np.count_nonzero(check_array == 0, axis = 0)
    null_number = np.argwhere(null_count == null_count.max())

    
    task3.write("\nMost skipped answers to the question:" + str(null_number) + \
                " - " + str(null_number.max()) + " skips - " + \
                    str(round((null_number.max() / valid_rows),2) * 100) + "%")

    bad_count = np.count_nonzero(check_array == -1, axis=0)
    bad_number = np.argwhere(bad_count == bad_count.max())
    task3.write("\nMost incorrect answers to the question:" + str(bad_number) + \
                " - " + str(bad_number.max()) + " wrong turns - " + \
                    str(round((bad_number.max() / valid_rows),2) * 100) + "%")
          