class Student:
    def __init__(self,name,student_id,age,marks):
        self.name=name
        self.student_id=student_id
        self.age=age
        self.marks=marks

    def display(self):
        print("Student name:",self.name)
        print("Student id:",self.student_id)
        print("Student age:",self.age)
        print("Student marks:",self.marks)

class StudentManagementSystem:
    def __init__(self):
        self.students=[]

    def add_student(self):
        student_id = input('enter the student_id:')
        sname = input('enter the name:')
        age = int(input('enter the age:'))
        marks = float(input('enter the marks:'))
        student = Student( sname,student_id,age,marks)
        self.students.append(student)

    def view_students(self):
        if len(self.students)==0:
            print("No student found!")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        student_id =input('enter  the id')
        for s in self.students:
            if s.student_id == student_id:

                print("Student found")
                return s.display()
        print("Student not found")

    def update_marks(self):
        student_id =input('enter  the id:')
        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("enter new marks :"))
                student.marks = new_marks
                return "marks updated successfully"
        print("Student Not Found")    
    
    def delete_student(self):
        student_id =input('enter  the id:')
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully")
                return
        print("Student not Found")

    def display_topper(self):
        topper = self.students[0]
        for student in self.students:
            if student.marks > topper.marks:
                topper = student
        print("\n Topper Details")
        topper.display()
 
sms = StudentManagementSystem()
while True:
    print('---------------Student Management Systerm-----------------')
    print('1.add_student')
    print('2.view_students')
    print('3.search_student')
    print('4.update_marks')
    print('5.delete_student')
    print('6.display_topper')

    choice = int(input("enter your choice :"))

    if choice == 1:
        sms.add_student()

    elif choice == 2:
        sms.view_students()

    elif choice == 3:
        sms.search_student()

    elif choice == 4:
        sms.update_marks()

    elif choice == 5:
        sms.delete_student()

    elif choice == 6:
        sms.display_topper()
        break 
    else:  
        print("Invalid choice")
        




    





            






 


    

        

        
        



    


            
        

    


    

    



