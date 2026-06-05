marks=[46.2,65.2,98.1,45.9,96.4,23.7,64.0]
print(marks)
print(type(marks))
print(marks[3])
info=["amit",98,"delhi"]
print(info)
info[0]="karan"
print(info)#list allows to do so
#same as of strings list will show us error if we will ask something out of index

str="oalj"
print(str[0])
#str[0]="ankit"
#string does not allow that whereas list allows us to change 

#list
list=[1,3,2,4,6,5,4]
list.append(7)
print(list)#append aka mutation
list.sort()
print(list)#sort asc
list.sort(reverse=True)
print(list)
list2=["banana","litchi","whyrat","apple"]
list2.sort(reverse=True)#sort des
print(list2)
list.reverse()
print(list)#reverse
list.insert(3,117)
print(list)
list.remove(4)
print(list)
list.pop(4)
print(list)

#tupples
tup=(9,3,4,6,9,3)
print(type(tup))
t=(1,)
print(t)
print(tup.index(3))
print(tup.count(9))

#pq1
s=input("movie 1: ")
a=input("movie 2: ")
d=input("movie 3: ")

list=[s,a,d]
print(list)

#pq2
list3 = [1,"abc","abc",1]

r = list3[::-1]

if r==list3:
    print("p")
else:
    print("np")


#pq3
tup = ("c","d","a","a","b","b","a")
print(tup.count("a"))
list6 = ["c","d","a","a","b","b","a"]
list6.sort()
print(list6)
