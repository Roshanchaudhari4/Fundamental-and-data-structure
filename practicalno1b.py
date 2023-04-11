#In second year computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football.
#Write a Python program using functions to compute following: -
#a)	List of students who play both cricket and badminton
#b)	List of students who play either cricket or badminton but not both
#c)	Number of students who play neither cricket nor badminton
#d)	Number of students who play cricket and football but not badminton.
#(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)


def intersection(list1,list2):
    rr=[]
    for student in list1:             # jar list 1 madhle student list 2 madhe present astil tar append kara list2
        if student in list2:          # those are common in list1 or list 2
            rr.append(student)
    return rr
    

def union(list1,list2):
    rr=list2.copy()
    for student in list1:            #je list1 madhe present ahe pan list2 madhe present nahi
        if not student in list2:
            rr.append(student)
    return rr

def diff(list1,list2):
    rr=[]
    for student in list1:            
        if not student in list2:
            rr.append(student)
    return rr
            

    
a=[]
b=[]
c=[]
l=int(input("Enter no of player who play cricket:"))
for i in range(l):
    e=input("Enter the name of player:")
    a.append(e)
    
m=int(input("Enter no of player who play badminton:"))
for i in range(m):
    f=input("Enter the name of player:")
    b.append(f)
    
n=int(input("Enter no of player who play football:"))
for i in range(n):
    g=input("Enter the name of player:")
    c.append(g)
    
print("cricket",a)
print("badminton",b)
print("footbaall",c)
    
print("Enter the number of player who play both cricket and badminton",intersection(a,b))
print("Enter the number of player who play either cricket or badminton but not both",diff(union(a,b),intersection(a,b)))
print("Enter the number of player who play neither cricket nor badminton",diff(diff(c,b),a))
print("Enter the number of player who play cricket and football but not badminton",diff(union(a,c),b))

