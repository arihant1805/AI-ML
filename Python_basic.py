# age =int(input())
# # F string
# print(f"Your age is {age}")


# print(False or [])

# name = "Bea"u"  //This is wrong
# name1 = "bea\"u"  
# name2 ='bea"u'
#  print(name1==name2)

# #  any([statement1,statement2,..])= if statement1 or statement2 or ...
# #   all([statement1,statement2,..])= if statement1 and statement2 and ...

# # COMPLEX NO
# num1= 2+3j
# num2=complex(2,3)
# print(num1==num2)
# print(f"{num1.real}+{num2.imag}j")

# # NUMBER FUNCTION
# num1=5.645
# print(round(num1,2))

# # LIST
# A=["Hii","Hello"]
# A.append("Jai jinendra")
# A.extend(["for","more","than","one"])
# A.remove("for")
# A.insert(-1,"last")
# lastWord=A.pop()
# A+=["for","more","than","one"]
# print(A[3:])
# A.sort()
# A.sort(key=str.lower)
# new_sorted_list=sorted(A,key=str.upper)


# # TUPLES : it can't be modified
# T1=("Hii","Hello")
# T1.index("Hii")
# T2=T1+("Jai jinendra")
# # T1+=("Jai jinendra") it will throw an error since tuples can't be modified
# print(T2)
# print(T1)


# # DICTIONARY
# # kind of HashMap in python
# Hs={"arihant":18,"Prachi":20}
# print(Hs.keys())
# print(f"Arihant's age is {Hs['arihant']}")
# print(isinstance(Hs,dict))
# print(type(Hs))
# Hs.get("prachi",29)
# Hs.get("Prachi")
# Hs.pop("arihant")
# Hs.popitem()
# Hs["New item"]="some thing new"
# print(Hs)
# del Hs("New item")

# # SETS
# Set1={1,2,3}
# Set2={3,4,5,6}

# intersection=Set1 & Set2
# Union=Set1 | Set2
# diff=Set1-Set2
# isSubset=Set1<Set2
# print(isSubset)
# Set1.remove(2)
# Set1.remove(1)
# isSubset=Set1<Set2
# print(isSubset)


# # FUNCTIONS
# def func(x=0):
#     print(x)
#     return x-1,x,x+1
# a,b,c=func(2)
# func()
# print(a+b+c)
# # Any im-mutable thing will not change in the function but the mutable will change
# # Nested function
# def one(y):
#     def two(x):
#         # to tell about which variable we are talking of to use it inside any nested function
#         nonlocal y
#         y=y+1
#         print(x+y)
#     two(3)
#     two(1+y)
# one(3)


# # OBJECTS
# x=0
# print(f"This func will return the address of x which is {id(x)}")


# # Loops
# item={12,23,34}
# for index,item in enumerate(item):
#     print(f"{item} have {index} index")


# # CLASSES
# class Activity:
#     def act(self):
#         print("we act to spend time")
# # inheritance   Activity is parent class and learn is inherited class 
# class learn(Activity):
#     # constructor
#     def __init__(self,method,time):
#         self.method=method
#         self.time=time
#     def online(self,hours):
#         if hours>3:
#             print("Amazing")
    
# ansh=learn("online",3)
# print(ansh.method,ansh.time)
# ansh.online(4)
# ansh.act()


# # MODULES
# from module import Sample
# Sample()
# from math import sqrt
# print(sqrt(1600))


# # LAMBDA FUNCTIONS
# SQRT=lambda num:num**.5
# print(SQRT(4))

# map(), filter() and reduce()

# # DECORATORS 
"""Here @before is a decorator which is a function which 
   has a inner function and return the inner funtion"""  
# def before(f):
#     def inner_func():
#         print("inner function has called")
#         return f()
#     return inner_func

# @before
# def hello():
#     print("hello")
# hello()


# # ANNOTATIONS
#  def sum(x:int,y:int)->int :
#     """Here we have defined that the function will 
#         take integer and return integer """
#     return x+y


# # EXCEPTIONS
# try:
#     result=2/0
# except ZeroDivisionError:
#     print("Can't divide by zero")
# finally :
#     result=1
# print(result) # 1
"""We can also raise the error statement"""
# try:
#     raise Exception('It will print the error written here')
# except Exception as error:
#     print(error)

# class ErrorNotFound(Exception):
#     print("It is a class with exception")
#     pass
# try:
#     raise ErrorNotFound()
# except ErrorNotFound:
#     print("Error not found")


# # LIST COMPRESSION
# list1=[1,2,3,4,5]
# list2=[n**2 for n in list1]
# print(list2)

# # OPERATOR OVERLOADING
# class stud:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __gt__(self,other):  # here gt means greater than
#         return True if self.age>other.age else False
# Arihant = stud("Arihant",18)
# Archit=stud("Archit",20)
# print(Archit>Arihant)



