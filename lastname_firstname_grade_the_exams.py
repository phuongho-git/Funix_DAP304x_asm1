
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

# Task 2.2: Xử lý chuỗi
       for rowno in range(row_count):
           exam = exams[rowno].strip()
           answer = exam.split(",")
           id = answer[0]
           invalid_lines = []

           # Task: 2.2: Báo cáo tổng số dòng không hợp lệ và in các dòng đó

           if (len(answer)!=26):
               print("\nInvalid line of data: does not contain exactly 26 values:\n", exam)

           elif ( len(id) != 9 and id[0] != "N" and id[1:10] != ["0","1", "2", "3","4","5","6","7","8","9"]):
               print("\nInvalid line of data: N# is invalid\n", exam)

           else:
               print("\nTotal invalid lines of data: 0")

           


