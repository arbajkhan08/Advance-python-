# try:
#     with open("1.txt", "r") as f:
#         print(f.read())
        
# except Exception as e:
#     print(e)
# try:
#     with open("2.txt", "r") as f:
#         print(f.read())
        
# except Exception as e:
#     print(e)
# try:
#     with open("3.txt", "r") as f:
#         print(f.read())

# except Exception as e:
#     print(e)


# print("Thank you")    

# write a program to print 3 ,5, 7 from list using enumerate function


# l = [1,2,3,4,5,6,7,8]

# for i, item in enumerate(l):
#     if i == 2 or i == 4 or i == 6:
#         print(item)


# write a list compreshension to print a list which contian the multiplilcation table of user entred number


# n = int(input("enter a number "))
# table = [n*i for i in range(1,11)]
# print(table)


# try:
#     a = int(input("enter a: "))
#     b = int(input("enter b: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("Infimnte")    


#  store the mutltiplicstion table generated in problem file . txt

n = int(input("enter a number "))
table = [n*i for i in range(1,11)]

with open("table.txt", "a") as f:
    f.write(str(table)+ "/n")
