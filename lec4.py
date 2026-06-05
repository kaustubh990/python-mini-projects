#dictionary in python
info = {
    "key" : "value",
    "name" : "kaustubh",
    "surname" : "yadav",
    "hs" : 90,
    "subjects" : ["eng","hindi","pe","phy","chem","maths"],
     "today's topics" : ("dict","sets"),
     12 : 928
}

#basically just like list dictionary is also mutable and since tupple cannot be changed hence it can be made a key
#value can accept any datatype list,tupple but key cannot accept list or tupple, dict doesn't allow duplicate values
print(info)
print(type(info))



print(info["hs"])
print(info["name"])
info["name"]="harshit"
print(info)

null_dict = {}
print(null_dict)
null_dict["name"]="amit"
print(null_dict)

#nested dict
student = {
    "name" : "kaustubh yadav",
    "subjects" : {
        "phy" : 98,
        "chem" : 99,
        "maths" :97,
    }
    }

print(student)
print(student["name"])
print(student["subjects"]["phy"])
print(list(student.keys()))#.keys
print(len(list(student.keys())))#lenght of keys
print(len(list(student.values())))#.values
print(list(student.values()))
print(student.items())#.items
pairs= list(student.items())
print(pairs[1])
print(student["name"])
print(student.get("name"))
#print(student["name2"])#error
#print(student.get("name2"))#none
student.update({"city" : "delhi"})#method1
print(student)
new_dict = {"city" : "delhi", "age": 44, "name" : "amit" ,}
student.update(new_dict)
print(student)#method2


#sets in python
#list and dict cant be stored in set as both of them are mutaable
#imp point= sets are mutaable but elements of sets are immutable
collection = {1,2,3,4,4,"hello","appy","appy"}
print(collection)
print(type(collection))#we will get out different everytime , it neeeds not to be true that it will came in same manner as we have written
#if we have written somethingmore than once it won't give a error but it will remove it and show it once
print(len(collection))#total number of items
coll={}
print(type(coll))#syntax of empty dict
coll=set()
print(type(coll))#syntax of empty set
coll.add(3)
coll.add(1)
coll.add(8)
coll.add(3)#add
coll.remove(3)#remove
coll.add("kkkkk")
coll.add((1,2,3))
coll.pop()
#coll.clear()#clear
print(coll)

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))

#pq1
word_meanings = {
    "table" : ["a piece of furniture","list of facts&figures"],
    "cat" : "an animal",
}
print(word_meanings)

#pq2
sub={"python","java","c++","js","java","python","java","c++","c"}
print(len(sub))

#pq3
s1=int(input("marks1:"))
s2=int(input("marks2:"))
s3=int(input("marks3:"))

subjects = {}
subjects.update({"phy":s1})
subjects.update({"chem":s2})
subjects.update({"maths":s3})

print(subjects)

#pq4
values={9,"9.0"}

print(values)