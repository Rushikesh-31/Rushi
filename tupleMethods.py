#RUSHIKESH BANDIWADEKAR, SE-IT, A-37
#Program to perform operations on tuple

#Creating empty list (as tuple is immutable we convert list into tuple later)
list = []

#Taking size/total number of elements to be added in tuple
num = int(input("Enter size of the tuple : "))
print("Enter elements to be added in tuple")

#Firstly we add elements in list
for i in range(0,num):
    i = input()
    list.append(i)

#Converting list to tuple
tuple = tuple(list)

#Asking user to enter element of which index to be find
ele = input("Enter element of which index to be find : ")

#Checking element is present or not and if present displaying its position/index
if ele in tuple:
    print(f"Element {ele} is found at position",tuple.index(ele)+1)
else:
    print(f"Element {ele} is not present in tuple")

#Finding length of tuple
print(f"Length of the tuple is {len(tuple)}")

#Taking upper bound and lower bound to slice tuple
low = int(input("Enter lower bound from where slicing will start : "))
high = int(input("Enter upper bound upto which slicing to be done (Exclusive) : "))

#Printing sliced tuple
print(tuple[low:high])