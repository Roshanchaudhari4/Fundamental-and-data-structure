#Experiment no 9:write a pjyton program to compute following computation on matrices:
#a)addition of two numbers
#b)subtration of two number
#c)multiplication of two matrix
#d)transpose of a matrix



x=[[1,2,3],
  [4,5,6],
  [7,8,9]]

y=[[10,11,12],
  [13,14,15],
  [16,17,18]]

result=[[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(x)):                      
        for j in range(len(x[0])):      
               result[i][j]=x[i][j]+y[i][j]  
for r in result:
               print("addition of matrix is:",r)


for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]-y[i][j]
for r in result:
              print("subtraction of matrix is:",r)


for i in range(len(x)):                      
        for j in range(len(x[0])):      
               result[i][j]=x[i][j]*y[i][j]  
for r in result:
               print("multiplication of matrix is:",r)



for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]=x[i][j]
for r in result:
              print("transpose of matrix is:",r)






