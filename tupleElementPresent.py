#RUSHIKESH BANDIWADEKAR, SE-IT, A-37
#Program to check element is present in tuple

#Creating empty list (as tuple is immutable we convert list into tuple later)
list = []

#Taking size/total number of elements to be added in tuple
num = int(input("How many elements you wanted to add in tuple : "))
print("Enter elements to be added in tuple")

#Firstly we add elements in list
for i in range(0,num):
    i = input()
    list.append(i)

#Converting list to tuple
tuple = tuple(list)

#Asking element to be searched
ele = input("Enter element to be searched in tuple : ")

#Checking element is present or not in tuple
if ele in tuple:
    print(f"Element {ele} is present in tuple")
else:
    print(f"Element {ele} is not present in tuple")