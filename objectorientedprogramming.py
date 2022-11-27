#static functions
class Math: 
    
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def pr():
        print("Run")
    
print(Math.add5(5))
Math.pr()


#Class attributes and class methods 

class person: 
    number_of_people = 0 
    GRAVITY = -9.8
    
    def __init__(self, name):
        self.name = name 
        person.add_person()
        
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people   
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
p1 = person("Tim")
p2 = person("Jim")
print(person.number_of_people_())




class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what to say")

class cat(pet):
    
    def __init__(self, name, age, color):
        super().__init__(name, age) # Calls the parent class name and age 
        self.color = color
        
    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I have {self.color} hair.")

class dog(pet):
    def speak(self):
        print("Bark")

p = pet("Toby", 5)
p.speak()
c = cat("Jinx", 7, "Black")
c.show()
d = dog("Jim", 16)
d.speak()


class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("Meow")


class dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("Bark")
   


class Student: 
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100
        
    def get_grade(self):
        return self.grade
    
class Course: 
    
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()
            
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Brian", 27, 60)
s3 = Student("Clay", 31, 87)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
#course.add_student(s3) #Adding this student would make differences to the list of studends 
        
print(course.get_average_grade())






class dog:
    
    #all params pass through this first ( initialization )
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    # functions in a class are called methods 
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
        
    def set_age(self, age):
        self.age = age
        return age
    
# These are the objects 
d = dog("tim", 21)
print(d.get_name())
print(d.get_age())
print(d.set_age("25"))


d2 = dog("bill", 5)
print(d2.get_name())
print(d2.get_age())

d = dog()
d.bark()
print(d.add_one(10))
print(type(d.bark))
