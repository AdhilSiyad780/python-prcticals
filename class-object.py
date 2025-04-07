# class Students:
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age 

#     def printit(self):
#         return f'{self.name} is {self.age} olf'
    
# item = Students('alikutti',89)
# print(item.printit())


# class Greet:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         return f'hi welcome mr.{self.name}'

# item = Greet('sutehhs')
# print(item.greet())

# class Rectangle:
#     def __init__(self,l,w):
#         self.length = l 
#         self.width  = w 

#     def area(self):
#         print(f'teh area of the rectangle is {self.length * self.width}')
#     def parameter(self):
#         print(f'the parameter of the rectangel is {2*(self.length+self.width)}')

# item = Rectangle(5,3)
# item.area()
# item.parameter()


# class Banckac:
#     def __init__(self,name):
#         self.name = name 
#         self.balance = 0 

#     def add_amount(self,amount):
#         self.balance +=amount
#         print(f'{amount} has been deposited to your acount')

#     def withdraw(self,amount):
#         if self.balance<amount:
#             print('not enough balance')
#         else:
#             self.balance-=amount
#             print(f'{amount} debited from your account successfully')

#     def check_balance(self):
#         print(f'your current balance is {self.balance}')

# item = Banckac('ali')
# item.add_amount(500)
# item.check_balance()
# item.withdraw(50)
# item.check_balance()



