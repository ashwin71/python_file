#List is mutable, ordered, and allows duplicate elements.

mylist1 = [1,2,3,4,5]
mylist2 = ["ashwin","krishna","karichery"]
mylist3 = [1,"ashwin",True,"ashwin"]
mylist4 = []

print(mylist1[0])
print(mylist1[1])
print(mylist1[-1])

#printing every element in list
for item in mylist2:
    print(item)

#checking a specific item in the list
if 1 in mylist1:
    print("yes")

#length of list 
print(len(mylist1))