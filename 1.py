"""
Exercise 1
answer:Yes


Exercise 2
answer:with the help of the negative index in Python ,we can access the elements of the list from the bottom.


Exercise 3
answer:list=[45,-3,16,8]


Exercise 4
answer:
(a) lst[0]
(b) lst[3]
(c) 10
(d) 29
(e) -4
(f) 29
(g) 10
(h) illegal


Exercise 5
answer:
(a) 3
(b) 5
(c) 1
(d) 5
(e) 5
(f) 2
(g) 0
(h) 3


Exercise 6
answer: Function len


Exercise 7
answer: a=[]


Exercise 8
answer:
(a) [20,1,-34,40,-8,60,1,3]
(b) [20,1,-34]
(c) [-8,60,1,3]
(d) [-8,60,1,3]
(e) [40,-8]
(f) [20,1,-34]
(g) [-8,60,1,3]
(h) [20,1,-34,40,-8,60,1,3]
(i) [20,1,-34,40]
(j) [1,-34,40,-8]
(k) True
(l) False
(m) 8


Exercise 9
answer:
(a)lst[0:5]=[2,4,8,10]
(b)lst[6:11]=[2,4,6,8,10]
(C)lst[7: ]=![2,4,6,8,10]
(d)lst[3:4]=['a','b','c']
(e)lst[ : ]
(f)lst[0:0]
(g)lst[-1: ]
(h)lst[ :3]
(i)lst[2: ]
(j)lst[1:4]=[ ]
(k)lst[1:4]


Exercise 10
answer:
(a) [8,8,8,8]
(b) [2,7,2,7,2,7,2,7,2,7,2,7]
(c) [1,2,3,'a','b','c','d']
(d) [1,2,1,2,1,2,4,2]
(e) [1,2,4,2,1,2,4,2,1,2,4,2]
 
Exercise 11
answer:
(a) [3,5,7,9]
(b) [50,60,70,80,90]
(c) [12,15,18]
(d) [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)]
(e) [(0,0),(0,2),(1,1),(1,3),(2,0),(2,2)]


Exercise 12
answer:
(a) [x**2 for x in range (1,6)]
(b) [x/4 for x in range (1,7)]
(c) [(x,y) for x in ['a','b'] for y in [0,1,2]]


Exercise 13
answer:
x in lst (show existence)
x not in lst (show not existence)


Exercise 14
answer:
reverse()function is used to reverse the order of objects in a list data structure in place.


Exercise 15
answer:
def sumlist(L):
    sum=0
    for m in L:
        if m>0:
            sum+=m
    return sum 
    
L=[]
for i in range (0,4):
    m=int(input("Enter a number of list:"))
    L+=[m]
    
z= sumlist(L) 
print(z,"the sum of positive numbers")
if len(L)==0:
    print("the list is empty")


Exercise 16
answer:
def count_evens(nums):
    count = 0
    for m in nums:
        if  n%2==0:
            count += 1
    return count
    
nums=[]
for i in range (0,4):
    m=int(input("Enter a number of list:"))
    nums+=[m]
    
    
print (count_evens(nums))


Exercise 17
answer:
def bigenough(lis):
    x = int(input("Enter a number as acompare:"))
    jadid=[]
    for i in lis:
        if  i>=x:
            jadid += [i]
    return jadid
    
lis=[]
for i in range (0,4):
    n=int(input("Enter a number of list:"))
    lis+=[n]
print (bigenough(lis))

Exercise 18
answer:
lst = [5, 3, 1] 
 
 
def next_number(lst): 
    my_max = 0 
    number = 0 
    for i in lst: 
        if i > my_max: 
            my_max = i 
 
    for i in range(1, my_max + 1): 
        if i not in lst: 
            return i 
 
    return my_max + 1 
 
 
print(next_number(lst))


Exercise 19
answer:
def reverse(lis):
    jadid=[]
    for i in lis[ ::-1]:
            jadid += [i]
    return jadid
    
lis=[]
for i in range (0,4):
    n=int(input("Enter a number of list:"))
    lis+=[n]
print (reverse(lis))


Exercise 20
answer:
z=[[1 for _ in range(9)]for _ in range(6)]
print(z)
z[2][4]=0
print(z)


Exercise 21
answer:
#first way 
lis = []
for i in range(1,11):
    lis +=[i]
print(lis)
#second way 
lis=[10,9,8,7,6,5,4,3,2,1]
new=[]
for i in lis[ ::-1]:
    new+=[i]
print(new)
#third way
lis = []
i = 0 
while i<10:
    i+=1 
    lis +=[i]
print(lis)
#forth way 
lis=[20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10,0]
new=[]
for i in lis[-11:-1:1]:
    new +=[i]
print(new)
#fifth way 
print("[1,2,3,4,5,6,7,8,9,10]")


Exercise 22
answer:
def matris 2 body(r):
    new_mat = [[0] * len(r)] * len(r)
    for i in range(len(r)):
        for j in range(len(r[0])):
            new_mat[j][i] = r[i][j]
    flag = 0
    for i in range(len(r)):
        for j in range(len(r)):
            if r[i] == new_mat[j]:
                flag = 1
    if flag:
        return True
    else:
        return False


Exercise 23
answer:
def check_winner(p):
    new_mat = [[0] * len(p)] * len(p)
    for i in range(len(p)):
        for j in range(len(p[0])):
            new_mat[j][i] = p[i][j]
    for i in m:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    for i in new_mat:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    if p[0][0] == p[1][1] == p[2][2] == 'X':
        return 'X'
    elif p[0][0] == p[1][1] == p[2][2] == 'O':
        return 'O'
    if p[0][2] == p[1][1] == p[2][0] == 'X':
        return 'X'
    elif p[0][2] == p[1][1] == p[2][0] == 'X':
        return 'O'
    return ' '
"""






