
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


def report(classFile):
    with open(classFile,"r") as readfile:
        with open("task2.txt","w") as task2:    

            exams = readfile.readlines()
            row_count = len(exams)      
            valid_lines = []


            with open("task4.txt","w") as task4:

                for rowno in range(row_count):
                    exam = exams[rowno].strip()
                    answers = exam.split(",")
                    id = answers[0]                   
           

                    # in các dòng không chứa 26 giá trị
                    if (len(answers) != 26):
                        task2.write("\nInvalid line of data: does not contain exactly 26 values:\n")
                        task2.write(exam)
                        task2.write("\n")

                    # in các dòng có N# không hợp lê
                    elif (len(id) != 9 
                        or id[0] != "N"
                        or id[1:10].isnumeric() == False):
               
                        task2.write("\nInvalid line of data: N# is invalid\n")
                        task2.write(exam)
                        task2.write("\n")

                    # tạo list các dòng hợp lệ
                    else:             
                        valid_lines += [answers]                                           
                        total_score = 0
                        answers.pop(0)                        

                        for answer in range(25):
                            if answers[answer] == right_answer[answer]:
                                score = 4
                                total_score += score                                

                            elif answers[answer] == "":
                                score = 0
                                total_score += score                                

                            else:
                                score = -1                         
                                                                                                                        
                        # in kết quả của mỗi học sinh
                        task4.write(id + "," + str(total_score) + "\n")

                        score_lines = np.array([id,total_score])
                        print(score_lines)
                        
                        


            # in thông báo nếu các dòng đều hợp lệ
            rows = len(valid_lines)
            if rows == len(exams):
                task2.write("\n\nNo errors found!")

            # ghi file report
            task2.write("\n\n*** REPORT ***\n")
            # in tổng số dòng 
            task2.write("\nTotal lines of data:" + str(row_count))
            # tổng số dòng hợp lệ
            task2.write("\nTotal valid lines of data:" + str(len(valid_lines)))
            # tổng số dòng không hợp lệ   
            task2.write("\nTotal invalid lines of data:" + str(row_count - len(valid_lines)))   

                                                  

classFile = "./Data/class2.txt"
report(classFile)                                                    