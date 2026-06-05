#oops
#class example 1
# class Student :              
#     #default constructor   
#     def __init__(self):
#         print("adding new student in database")
    
#                           #if possible start class name with capital
#                                                                                                        #name = "karan"         we r not maling everyones name karan
#    #parameterized constructor
#     name="anonymous"   #class attribute
#     college_name = "abc college"   #class attribute
#     def __init__(self,fullname,marks):       #here fullname is parameter                                                                #with the help of self para meter we can store diff vvariablesand diff datas
#         self.name=fullname    #same name ka class att or same ka obj att to obj att>class attr                 #yaha pe obj ke ander jo naya create hone wala h woname                                                        #or self me mtlb s1 me name ke ander jo ki naya variable h jiske ander full name ki value assign hojayegi
#         self.marks=marks
#         print("adding new student in database")
#    #the data and variables stores inside the class or obj is called attributes



                                                                                         #these parentheses()are used to call consstructors,,,,,,,,,,,,,,,,,jo bhi value yaha pass krenge wofull name me aaa jayegi



#class and instance attribute:   class h student ki jisme s1,s2,s3,s4 studenst h to inka naam alag hoga to ye object ya instance attrivut hoga uska self. krkke krenge or class attribute hoga jab hum class ke andar koi variable banate h jo ki sare students ke liye same hoga jaise ki school name,school address etc







# s1 = Student("karan",88) 
# print(s1.name,s1.marks)
# print(s1.college_name)
# s2 = Student("mintu",99)
# print(s2.name,s2.marks)
# print(Student.college_name)   #class attribute ko class name ke through bhi access kr skte h




# s2 = Student()
# print(s2.name)

# #example2
# class Cars : 
#     colour = "blue"
#     model = "mercedes"

# c1 = Cars()
# print(c1.colour)
# print(c1.model)


#constructor






#class is divided into methods and attributes (car ki brand,milegan,price etc) and methods (start,stop,accelerate etc)


# class Car :
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def start(self):
#         print("car started")
#     def stop(self):
#         print("car stopped")

# c1=Car("mercedes","s class",100000)
# print(c1.brand,c1.model,c1.price)
# c1.start()
# c1.stop()




#static method:  static method is a method which is not dependent on the object of the class and can be called without creating an object of the class. It is defined using the @staticmethod decorator.It is at the class level and can be called using the class name or an object of the class. Static methods do not have access to the instance (self) or class (cls) variables and are used for utility functions that do not require any data from the class or its instances.








#abstraction and encapsulation
class Car :
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")

c1=Car()
c1.start()   #this is abstraction because we are using the start method without knowing how it works internally. We just know that it will start the car when we call it. We don't need to know the details of how the car starts, we just need to know that it will start when we call the start method. This is abstraction because we are hiding the internal details of how the car starts and only exposing the necessary functionality to the user.



