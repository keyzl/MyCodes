
class Student(Person):
    def init(self, name, age, nation, kontrakti):
        Person.init(self, name, age, nation)
        self.kontrakti = kontrakti

    def get_student_info(self):
    # def get_info(self):
        return f'Ism: {self.name}, Yoshi: {self.age}, Millati: {self.nation}, Kontrakt: {self.kontrakti}'


obj1 = Person('ali', 21, 'Uzbek')
obj2 = Student('masha', 19, 'Qozoq', 25_000_000)
# print(obj1.get_info())
# print(obj2.get_info())
print(obj1.get_info())
print(obj2.get_info())
print(obj2.get_student_info())



class person (worker):
    def init(self, name, age, nation, oyligi):
        Person.init(self, name, age, nation)
        self.oyligi = oyligi

    def get_person_info(self):
    # def get_info(self):
        return f'Ism: {self.name}, Yoshi: {self.age}, Millati: {self.nation}, Kontrakt: {self.oyligi}'


obj1 = worker('kimdur', 35, 'Uzbek')
obj2 = dosti('marat', 40, 'qirgiz', 7_000_000)
# print(obj1.get_info())
# print(obj2.get_info())
print(obj1.get_info())
print(obj2.get_info())
print(obj2.get_student_info())




#conculyator
class calculator_implementation():
   def __init__(self,in_1,in_2):
      self.a=in_1
      self.b=in_2
   def add_vals(self):
      return self.a+self.b
   def multiply_vals(self):
      return self.a*self.b
   def divide_vals(self):
      return self.a/self.b
   def subtract_vals(self):
      return self.a-self.b
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))
print("The entered first and second numbers are : ")
print(input_1, input_2)
my_instance = calculator_implementation(input_1,input_2)
choice=1
while choice!=0:
   print("0. Exit")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   choice=int(input("Enter your choice... "))
   if choice==1:
      print("The computed addition result is : ",my_instance.add_vals())
   elif choice==2:
      print("The computed subtraction result is : ",my_instance.subtract_vals())
   elif choice==3:
      print("The computed product result is : ",my_instance.multiply_vals())
   elif choice==4:
      print("The computed division result is : ",round(my_instance.divide_vals(),2))
   elif choice==0:
      print("Exit")
   else:
      print("Sorry, invalid choice!")
print()