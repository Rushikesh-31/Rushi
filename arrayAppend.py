#RUSHIKESH BANDIWADEKAR, SE-IT, A-37
#Program to append element to the last of array 

from array import *

#Taking size of the array
num = int(input("Enter size of the array : "))

#Using array list
array = []

print("Enter elements in array : ")

#Taking values in array
for i in range(num):
    ele = input()        
    array.append(ele)

#Printing array befor adding element
print("Array before adding element is \n",array)

#Asking element to be append in the array
addElement = input("Enter element to be appended in array : ")

array.append(addElement)

#Printing array after element is appended
print(f"Array after appending element {addElement} is :\n",array)