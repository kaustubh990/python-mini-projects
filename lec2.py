str1="this is\t a string"#strings are defined under double quotes
str2='kaustubh'#all single and double and triple quotes can be used to for strings, it is used so that the other can be used to other form
str3= "hello.\n i am kaustubh"
print(str3)
print(str1)
final_str=str2+" "+str2
print(len(final_str)) 
print(final_str)
print(str1+str2)#concatenation is simply applied by using + operator
print(len(str2))#length of string len(str),spaces,special ch everything is counted in length
print(str2[3])#indexing, we cant modify ex, we cant replace empty space with something
print(str2[2:7])#slicing in string
print(str2[0:len(str2)])




str="this is a city"
print(str.endswith("ity"))#endswith
print(str.capitalize())#capitalise
print(str.replace("i","a"))#replace
print(str.replace("city","country"))
print(str.find("z"))#find
print(str.count("z"))






#pq=1
a=input("first name: ")
print(len(a))


#pq2
marks=int(input())

if(marks>=90 and marks<100):
    print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B")
elif(marks>=70 and marks<80):
    print("Grade C")
elif(marks<70):
    print("Grade D")

#hq2
a=int(input())
b=int(input())
c=int(input())

if(a>=b and a>=c):
    print("largest",a)
elif(b>=c):
    print("largest",b)
else:
    print("largest",c)

#hq3
x=int(input("num:"))

if(x%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")

    #palindrome
s=input("enter value: ")

r=s[::-1]

if(r==s):
    print("p")
else:
    print("np")