#RUSHIKESH BANDIWADEKAR, SE-IT, A-37
#Program to sort list and print only odd numbers from list

#Creating empty list
list = []

#Taking size/total number of elements to be added in list
num = int(input("How many numbers you wanted to add in list : "))
print("Enter numbers in list")

#Adding elements in the list
for i in range(0,num):
    i = int(input())
    list.append(i)

#Sorting elements from list
list = [x for x in list if x%2 != 0]

print("After removing even numbers list is :\n",list)