# x = 3
# y = 4
# print(x+y)

# x = input("what's your name?\n")
# print(x)

# x, y = input().split()
# print(x, y)

# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))
# if x > y:
#     print("X is greater")
# elif(x == y):
#     print("Both are equal")
# else:
#     print("Y is greater")

# i = 10
# while(i > 5):
#     print(i)
#     i-=1
# print("\n")
# for i in range(0,10,2): #it'll increase by 2, range(10) means all value 0-9
#     print(i, end = ' ')

# price = 400 #formated string
# print(f'The price of my Cube is {price} Tk')

# def sum(a, b = 10): #b = 10 is default parameter velue, if no b found, it will count 10
#     print("Sum is ", a+b)
# def pau(a, b):
#     return a**b
# x = 2
# y = 8
# sum(x)
# print(pau(x, y))

# lst = [1,2,3,4, "siyam", 24.4] #empty list: lst = [] or list()
# print(lst)
# print(lst[0], lst[5])
# print(lst[-6], lst[-1])
# lst.append(100)
# print(lst[-1])
# lst.insert(1, "wk") #wk is inserted in index 1
# print(lst)
# #
# lst2 = lst #or lst.copy()
# print(lst2)
# lst2.pop()
# print(lst2)
# lst2.pop(3) #index 3 is poped
# lst2.reverse()
# print(lst2)

# tp = () #empty tuple created or tp = tuple()
# tp = (1,2,3,4) #same as list but not dynamic as list, it is unchangeable once it is created
# print(tp)
# tp += (8,9) #adding some extra elements
# print(tp[3]) 
# #tp[3] = 10, not possible index 3 in unchangeable once it is created
# for i in range(len(tp)):
#     print("Index", i , ":", tp[i])

# lst1 = [1,2,"wk",4,5]
# lst_nw = lst1[1:4] #slicing 1 to ahead of index 4; lst1[:]_full list
# lst_mw = lst1[1:5:2] #slicing index increasing by 2
# print(lst_nw)
# print(lst_mw)


# lst = [6,4,8,1,20,3,1]
# lst.sort()
# print(lst)
# lst1 = [6,4,8,1,20,3,1]
# lst2 = sorted(lst1) #not lossing the previous lst1
# print(lst1)
# print(lst2)
# print(lst1.index(1)) #it will find index of 1st occurance of value 1

# v = [1,2,3,4,5,6]
# mul = [v[i]*2 for i in range(len(v))] #list comprehension
# #print(mul)
# even_add = [v[i]+2 for i in range(len(v)) if v[i]%2 == 0]
# print(even_add)

# n = []
# n = input().split()
# print(n)
# n = [int(n[i]) for i in range(len(n))] #converting list value string to int
# print(n)
#or
# lst = [int(x) for x in input().split()]
# print(lst)
#or
# lst = list(map(int, input().split()))
# print(lst)

# N = int(input("Enter the size of the list: "))   ## N num of list input
## Taking N numbers as input and creating the list using list comprehension
# numbers = [int(input(f"Enter number {i+1}: ")) for i in range(N)]
# print("The list is:", numbers)

# llst = [10,20,30,40],[50,60,70,80],[11,22,33,44]
# print(llst)
# print(llst[2][1])
# for i in llst:
#     for j in i:
#         print(j, end = ' ')
#     print()

# student_id = set() #declearing a set
# student_id1 = {101, 102, 103, 103}
# student_info = {"wk", 24, "Dhaka", 18}
# student_id1.add(120) #unordered
# print(student_id1) #only contain unique value
# #student_id1.discard(102)
# #or
# student_id1.remove(102)
# print(student_id1)
# student_id1.add(104)
# print(student_id1)
# student_id.update(student_info)
# print(student_id)
# print("wk" in student_info)
# print("wk" in student_id1)

#new = dict() or {} #creating an empty dictionary
# country = {
#     "Germany" : "Berlin",
#     "Canada" : "Torrento",
#     "England" : "London",
# }
# print(country)
# print(country["England"],"\n")
# #country["Bangladesh"] = "Dhaka"
# #or
# country.update(({"Bangladesh": "Dhaka"}))
# del country["England"]
# #print(country)
# #or
# for capi in country:
#     print(f'{country[capi]} is the capital of {capi}')
# #or
# # for capi, cntry in country.items(): #iterate value-key pair through items()
# #     print(f'{capi} is the capital of {cntry}')
