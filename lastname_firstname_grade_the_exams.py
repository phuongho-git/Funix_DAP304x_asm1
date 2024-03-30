
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





# Task 2.1: Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp.

with open("./Data/class2.txt","r") as readfile:
   with open("task2.txt","a+") as task2:
       exams = readfile.readlines()
       row_count = len(exams)
       print("Total valid lines of data:", row_count)


# Task 2.2 và 2.3: Báo cáo tổng số dòng không hợp lệ và không hợp lệ. In các dòng không hợp lệ.
       
       valid_lines = []
       for rowno in range(row_count):
           exam = exams[rowno].strip()
           answers = exam.split(",")
           id = answers[0]
           

           # in các dòng không chứa 26 giá trị
           if (len(answers) != 26):
               print("\nInvalid line of data: does not contain exactly 26 values:\n", answers)

           # in các dòng có N# không hợp lê
           elif (len(id) != 9 
               or id[0] != "N"
               or id[1:10].isnumeric() == False):
               
               print("\nInvalid line of data: N# is invalid\n", answers)

           # tạo list chứa các dòng hợp lệ
           else:              
               valid_lines = valid_lines + [answers]                

       print("\nTotal valid lines of data:", len(valid_lines))   # in tổng số các dòng hợp lệ
       print("\nTotal invalid lines of data:", row_count - len(valid_lines))   #in tổng số các dòng không hợp lệ 


# Task 3:
       
# đáp án
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
right_answer = answer_key.split(",")

# chấm điểm
with open("./Data/task3.txt","w") as task3:           

    score_list = []
    for rowno in range(25):
        
        if valid_lines[i] == right_answer[i]:
            score_list.append(4)

        else:
            score_list.append(-1)
               
    print(right_answer[3])





      
           


