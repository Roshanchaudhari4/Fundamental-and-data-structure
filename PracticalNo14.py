#experiment no 14 write a phyton program to store first year percentage of student in an array.
#write function for sorting arry of floating point numbers in ascending order using
# a) selection sort b) bubble sort and display top five scores.







#selection sort
array=[]
def selection_sort(array):
    for i in range(len(array)):
        min=i
        for j in range(i+1,len(array)):
            if (array[j]<array[min]):
                min=j
                (array[i],array[min])=(array[min],array[i])
                
#bubble sort
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if (array[j]>array[j+1]):
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp

def entry():
    n=int(input("Enter the total number of stdent:"))
    for i in range(n):
        a=float(input("Please enter your percentage:"))
        array.append(a)
    return(array)

entry()


selection = int(input("\n1.selection sort\n2.bubble sort\n"))
if(selection==1):
    selection_sort(array)
    print("OUR TOPPERS:")
    for i in range(5):
        result = array[::1]
        print(result[i])

if(selection==2):
    bubble_sort(array)
    print("OUR TOPPER:")
    for i in range(5):
        result=array[::1]
        print(result[i])




