#functions

#function define
#method1
def calc_sum(a,b):    #here a and b are parameters
    sum=a+b
    print(sum)
    return sum

#func calling
calc_sum(2,3)    #here 2 and 3 are arguments
calc_sum(5426971266,98745215)

#method2
def calc_sum2(a,b):
    return a+b

print(calc_sum2(8763,23))

#function to calculate avg of 4 nums

def avg(a,b,c,d):
    return (a+b+c+d)/4
    
print(avg(4,5,9,5))

print("kaustubh",end=" ")#sep=" "
print("yadav")#end="\n


#pq1
def print_length (list):
    return len(list)

cities = ["hyd","chen","mum","kkr","lsg"]
print(print_length(cities))

#pq2
n_characters = ["naruto","jiraiya","rock lee","hinata"]

def print_list(list):
    for item in list:
        print(item,end="  ")

print_list(n_characters)

#logic for factorial of a number
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)


calc_fact(101)

#recursions
def show (n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(9)