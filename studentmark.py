n = int(input("Number student: "))
k = int(input("Number course:"))
studentID_list = []
studentname_list = []
studentDoB_list = []
courseID_list = []
coursename_list =[]
score_list = []
def add_student():
   
   for i in range(n):
      id = str(input("Student ID no "+ str(i+1)+":" )) 
      name = str(input("Student name no "+str(i+1)+": "))
      dob = str(input("Student DoB no "+ str(i+1)+ ":"))
      studentID_list.append(id)
      studentname_list.append(name)
      studentDoB_list.append(dob)
       
def add_course():
   
   for i in range(k):
      id = str(input("course ID no "+ str(i+1)+":" )) 
      name = str(input("Course name no "+str(i+1)+": "))
      courseID_list.append(id)
      coursename_list.append(name)
     
def add_score():
   for i in range(k):
      score = float(input("enter score of course"+ coursename_list[i]+ ": " ))
      score_list.append(score)

add_student()
add_course()
add_score()

print("LIST:")
print("student ID","student name", "student DoB", "course ID", "course name", "score")

for i in range(n):
   for j in range(k):
      print(f"""
{studentID_list[i]}, {studentname_list[i]}, {studentDoB_list[i]}, {courseID_list[j]}, {coursename_list[j]}, {score_list[j]}""")