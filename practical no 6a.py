

#Write a Python program to store roll numbers of student in array who attended training program in random order.
#Write function for searching whether particular student attended training program or not, using Linear search and Sentinel search






stud_list=[10,20,50,57,78,88,34]

def linear_search(arr,rollno):
    for i in range(len(stud_list)):
        if stud_list[i] == rollno:
            return i
        
    return -1

index=linear_search(stud_list,600)

if index == -1:
    print("in linear search student is not present")
else:
    print("in linear search student is present at position",index)


def sentinal_search(arr,rollno):
    last=arr[-1]
    i=0
    arr[-1]=rollno
    while(arr[i] !=rollno):
        i=i+1
    if  (i<arr[-1])or( last==rollno):
        return i
    else:
        return -1
    
index=sentinal_search(stud_list,78)


if index == -1:
    print("in sentinal search student is not present")
else:
    print("in sentinal search student is present at position",index)

