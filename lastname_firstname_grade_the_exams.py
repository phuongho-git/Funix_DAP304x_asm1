
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



# đáp án

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
right_answer = answer_key.split(",")

# Task 2.1: Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp.

with open("./Data/class2.txt","r") as readfile:
   with open("class1_grades.txt","a+") as writefile:
       exams = readfile.readlines()
       row_count = len(exams)
       print("Total valid lines of data:", row_count)

# Task 2.2: Báo cáo tổng số dòng không hợp lệ và không hợp lệ.
       
       valid_count = 0
       for rowno in range(row_count):
           exam = exams[rowno].strip()
           answer = exam.split(",")
           id = answer[0]

           # đếm các dòng có 26 giá trị và N# là mục đầu tiên, N# gồm ký tự N đầu tiên và 8 ký tự số phía sau.
           if (len(answer) == 26 
               & len(id) == 9 
               & id[0] == "N" 
               & id[1:10] == ["0","1", "2", "3","4","5","6","7","8","9"]):

               valid_count += 1

       print("\nTotal valid lines of data:", valid_count)
       print("\nTotal invalid lines of data:", row_count - valid_count)

# Task 3: In các dòng không hợp lệ ra báo cáo.
       for rowno in range(row_count):
           exam = exams[rowno].strip()
           answer = exam.split(",")
           id = answer[0]

           # in các dòng không chứa 26 giá trị
           if (len(answer) != 26):
               print("\nInvalid line of data: does not contain exactly 26 values:\n", answer)

           elif (len(id) != 9 
               & id[0] != "N" 
               & id[1:10] != ["0","1", "2", "3","4","5","6","7","8","9"]):
               print("\nInvalid line of data: N# is invalid\n", answer)      
           


