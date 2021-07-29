#RUSHIKESH BANDIWADEKAR, SE-IT, A-37
#Program to traverse through given dictionaries using for loop

#Taking how many data/values user want to enter/add in dictionary
n = int(input("Enter how many number of datas you want to add in dictionary : "))

#Creating empty dictionary
d = {}

#We take rolll number and name as key and values in this example
for i in range(n):
    keys = int(input("Enter roll number : "))
    values = input("Enter name of student : ")
    d[keys] = values

print("Values of dictionary are :")
print(d)