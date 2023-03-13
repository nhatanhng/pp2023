class student_info:
    def __init__(self):

        self.__name = 0
        self.__dob = 0
        self.__id = 0
   
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self,dob):
        self.__dob = dob

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id       


class course_info:
    def __init__(self):
        self.__name = 0
        self.__id = 0

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id    

        
class mark_info:
    def __init__(self):
        
        self.__mark = 0

    def get_mark(self):
        return self.__mark
    
    def set_mark(self, mark):
        self.__mark = mark


class school:
    def __init__(self):
        self.mark_list = []

        self.studentid_list = []
        self.studentname_list = []
        self.studentdob_list = []

        self.courseid_list = []
        self.coursename_list = []

    
        self.__num_student = 0
        self.__num_course = 0

    def set_num_course(self, num_course):
        self.__num_course = num_course

    def get_num_course(self):
        return self.__num_course
    
    def set_num_student(self, num_student):
        self.__num_student = num_student

    def get_num_student(self):
        return self.__num_student    

    def add_num_student(self):
        n = int(input("Enter number of student: "))
        self.set_num_student(n)

    def add_num_course(self):
        n = int(input("Enter number of course: "))
        self.set_num_course(n)

    def add_course(self):
        self.add_num_course()
        n = int(self.get_num_course())

        course = course_info()

        for i in range(n):    
            name = str(input("enter course"+str(i+1)+"'s name: "))
            id = str(input("enter course"+str(i+1)+"'s ID: "))
            
            course.set_name(name)
            course.set_id(id)
            
            self.coursename_list.append(course.get_name())
            self.courseid_list.append(course.get_id())

            # print(course.coursename_list[i])
    
    def add_student(self):
        self.add_num_student()
        student_num = int(self.get_num_student())


        student = student_info()

        for i in range(student_num):    
            name = str(input("enter student"+str(i+1)+"'s name: "))
            dob = str(input("enter student"+str(i+1)+"'s DoB: "))
            id = str(input("enter student"+str(i+1)+"s ID: "))

            student.set_name(name)
            student.set_dob(dob)
            student.set_id(id)
            
            self.studentname_list.append(student.get_name())
            self.studentid_list.append(student.get_id())
            self.studentdob_list.append(student.get_dob())

            # print(student.studentname_list[i])

    def add_mark(self):
        n = int(self.get_num_course())

        mark = mark_info()
    
        for i in range(n):
            score = (input("Enter score of course "+ self.coursename_list[i]+ ": "))
            mark.set_mark(score)
            self.mark_list.append(mark.get_mark())

    def display(self):
        m = mark_info()
        n = int(self.get_num_course())
        k = int(self.get_num_student())
        
        print("\nINFORMATION: \n")

        for i in range(k):
            print("Student no "+str(i+1)+" ID: "+self.studentid_list[i])
            print("Student no "+str(i+1)+" name: "+self.studentname_list[i])
            print("student no"+str(i+1)+" DoB: "+self.studentdob_list[i])     

        for i in range(n):
            print("course no "+str(i+1)+" ID: "+self.courseid_list[i])
            print("course no "+str(i+1)+" name: "+self.coursename_list[i])

        for i in range(k):
            for j in range(n):
                print("score of course "+ self.coursename_list[j]+" of student: "+ self.studentname_list[i]+" ID: "+ self.studentid_list[i]+": "+ self.mark_list[j])

s= school()
s.add_student()
s.add_course()
s.add_mark()
s.display()