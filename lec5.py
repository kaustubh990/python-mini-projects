#loops
i=1#iterator
while i<=6 :
    print("h",i)#iteration
    i+=1

#print num from 1 to 5
i=0
while i<=10 :
    print(i)
    i+=1

#loop kijo cond h wo variable value pe depend kregi

#reverse
i=5
while i>=0 :
    print(i)
    i-=1

#pq1 multiplication table of n
n=int(input("n = "))
i=1
while i<=10 :
    print(n*i)
    i+=1 

#pq2  
i=1
while i<=10 :
    print(i*i)
    i+=1

list = [1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(list) :
    print(list[idx])
    idx+=1

#pq3
list = (1,4,9,16,25,36,49,64,81,100)

x=81



i=0
while i < len(list) :
    if(list[i]==x):
        print("found at idx",i)
    else:
        print("finding")
    i+=1



#break and cont 
i=1
while i<=5 :
    
    if(i==5):
        i+=1
        break     #exit
    print(i)
    i+=1

i=1
while i<=5 :
    
    if(i==2):
        i+=1
        continue   #skip 
    print(i)
    i+=1

#for loop

list = [1,2,3,4,5,6]
vsggies = ["l","p","i","p" ]

for val in vsggies:
    print(val)


tupple = (1,2,3,4,5,6)
for value in tupple:
    print(value)

strings = "kautubh yadav"
for val in strings:
    print(val)

list1 = [1,4,9,16,25,36,49,64,81,100]

for index in list1:
    print(index)

#range function
print(range(6))
seq = range(6)
for i in seq:
    print(i)

print(range(2,20))
for i in range(2,20):
    print(i)

print(2,20,4)
for i in range(2,20,4):
    print(i)
