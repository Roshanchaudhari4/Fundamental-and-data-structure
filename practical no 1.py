#write a phyton program to store marks stored in subject "fundamental of data structure" by N student in the class write function to compute the following
#1.average score of class
#2.highest scre of  class
#3.count of student who are absent for the test
#4.display the mark with highest frequency







def average(a):
    sum=0
    count=0
    for i in range(len(a)):
        if (a[i]!=0):
            sum=sum+a[i]
            count=count+1
    print("average of the class is",sum/count)


def highest_score(a):
    for i in range(len(a)):
        max=a[0]
        break
    for i in range(1,len(a)):
        if (a[i]>max):
            max=a[i]
    print("highest score is:",max)
    return max

def lowest_score(a):
    for i in range(len(a)):
        min=a[0]
        break
    for i in range(1,len(a)):
        if (a[i]<min):
            min=a[i]
    print("Lowest score is:",min)
    return min

def absent(a):
    count=0
    for i in range(len(a)):
        if(a[i]==-1):
           count=count+1
    print("total absent student is :",count)

a=[]
total_students= int(input("Enter total number of student:"))
for i in range(total_students):
    a.append(
        (int(input("Enter the marks of the student:"))))

print(a)
absent(a)
average(a)
highest_score(a)
lowest_score(a)
    
