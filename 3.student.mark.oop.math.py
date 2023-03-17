import math
import numpy as np

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
        self.__credit = 0
        self.__name = 0
        self.__id = 0

    def get_credit(self):
        return self.__credit

    def set_credit(self, credit):
        self.__credit = credit

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


class Utils:
    def input_something(args):
        return int(input(f"Enter the number of {args}: "))


class school:
    def __init__(self):
        self.mark_list = []

        self.studentid_list = []
        self.studentname_list = []
        self.studentdob_list = []

        self.courseid_list = []
        self.coursename_list = []
        self.coursecredit_list = []

        self.gpa_avr_list = []
        self.gpa_avr_arr = 0


        self.credit_arr = 0 
        self.gpa_arr= 0
        self.gpa_avr = 0
        self.gpa_avr_arr = 0

        self.__num_student = 0
        self.__num_course = 0

        self.sum_credit = 0
        self.sum_mark_x_credit = 0

        self.dict_student_name = 0
        self.dict_student_id = 0
        self.dict_student_dob = 0
        self.dict_course_name = 0
        self.dict_course_id = 0
        self.dict_course_credit = 0
        
        
        self.order_student_name = 0
        self.order_student_id = 0
        self.order_student_dob = 0
        self.order_course_name = 0
        self.order_course_id = 0
        self.order_course_credit = 0

    def create_dict(self):
        self.dict_student_name = {key:value for key, value in zip(self.gpa_avr_arr,self.studentname_list)}
        self.dict_student_id = {key:value for key, value in zip(self.gpa_avr_arr,self.studentid_list)}
        self.dict_student_dob = {key:value for key, value in zip(self.gpa_avr_arr,self.studentdob_list)}


    def sort_desc_dict(self):
        self.order_student_name = dict(reversed(list(self.dict_student_name.items())))
        self.order_student_id = dict(reversed(list(self.dict_student_id.items())))
        self.order_student_dob = dict(reversed(list(self.dict_student_dob.items())))


    def print_order(self):
        print("\nORDERED GPA:")
        for i,j,k,l in self.order_student_name.values(),self.order_student_id.values(),self.order_student_dob.values(),self.gpa_avr_arr:
            print(f"Student name: {i} ID: {j} DoB: {k} Average GPA: {l}")

    def np_for_GPA(self):
        self.credit_arr = np.array(self.coursecredit_list) 
        self.gpa_arr = np.array(self.mark_list)

    def cal_GPA_avr(self): 
        for i in range(int(self.__num_course)):
            self.sum_credit = self.sum_credit + self.credit_arr[i]
            for j in range(0,self.__num_course,self.__num_student): #problem
                self.sum_mark_x_credit =0
                self.gpa_avr = 0                   
                for k in range(j,j+self.__num_student):
                    self.sum_mark_x_credit = self.sum_mark_x_credit + (self.gpa_arr[k] * self.credit_arr[i])
                    self.gpa_avr = self.sum_mark_x_credit / self.sum_credit   
                    self.gpa_avr_list.append(self.gpa_avr)
        self.gpa_avr_arr = np.array(self.gpa_avr_list)

    def set_num_course(self):
        self.__num_course = Utils.input_something("course")

    def get_num_course(self):
        return self.__num_course
    
    def set_num_student(self):
        self.__num_student = Utils.input_something("student")

    def get_num_student(self):
        return self.__num_student    

    def add_course(self):
        self.set_num_course()
        n = int(self.get_num_course())
        if (n<= 0):
            print("invalid number!")
        else:    
            course = course_info()

            for i in range(n):    
                name = str(input("\nEnter course"+str(i+1)+"'s name: "))
                id = str(input("Enter course"+str(i+1)+"'s ID: "))
                credit = int(input("Enter credit of course: "+str(i+1)+": "))
                
                course.set_name(name)
                course.set_id(id)
                course.set_credit(credit)
                
                self.coursename_list.append(course.get_name())
                self.courseid_list.append(course.get_id())
                self.coursecredit_list.append(course.get_credit())

    def add_student(self):
        self.set_num_student()
        student_num = int(self.get_num_student())
        if(student_num<=0):
            print("invalid number!")

        student = student_info()

        for i in range(student_num):    
            name = str(input("\nEnter student"+str(i+1)+"'s name: "))
            dob = str(input("Enter student"+str(i+1)+"'s DoB: "))
            id = str(input("Enter student"+str(i+1)+"s ID: "))

            student.set_name(name)
            student.set_dob(dob)
            student.set_id(id)
            
            self.studentname_list.append(student.get_name())
            self.studentid_list.append(student.get_id())
            self.studentdob_list.append(student.get_dob())

    def add_mark(self):
        mark = mark_info()
        n = int(self.get_num_student())
        for i in range(n):
            for j in range(int(self.get_num_course())):
                score = float(input(f"Enter GPA of course {self.coursename_list[j]} for student: {self.studentname_list[i]} ID: {self.studentid_list[i]}: "))
                mark.set_mark(math.floor(score))
                self.mark_list.append(mark.get_mark())

    def display(self):      
        n = int(self.get_num_course())
        k = int(self.get_num_student())
        
        print("\nINFORMATION: \n")

        for i in range(k):
            print("Student no "+str(i+1)+" ID: "+self.studentid_list[i])
            print("Student no "+str(i+1)+" name: "+self.studentname_list[i])
            print("student no"+str(i+1)+" DoB: "+self.studentdob_list[i])     
        
        for i in range(n):
            print("\ncourse no "+str(i+1)+" ID: "+self.courseid_list[i]) 
            print("course no "+str(i+1)+" name: "+self.coursename_list[i])
            print(f"course no {str(i+1)} credit: {self.coursecredit_list[i]}")
            print(f"course no {str(i+1)} GPA: {self.mark_list[i]}\n")
        
        for i in range(k):   
            
            print(f"Average GPA for student: {self.studentname_list[i]} ID: {self.studentid_list[i]}: {self.gpa_avr_list[i]}")
                          
s = school()
s.add_student()
s.add_course()
s.add_mark()
s.np_for_GPA()
s.cal_GPA_avr() 
s.display()
s.create_dict()
s.sort_desc_dict()
s.print_order()