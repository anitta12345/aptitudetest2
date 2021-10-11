def printDiagonalSums(mat, n):
 
    principal = 0
    secondary = 0;
    for i in range(0, n):
        for j in range(0, n):
 
            
            if (i == j):
                principal += mat[i][j]
 
            
            if ((i + j) == (n - 1)):
                secondary += mat[i][j]
         
    print("Sum of Diagonal:", principal)
n=int(input("enter value of limit"))
print("after entering value then click enter ")
a=[]
for i in range(n):         
   b =[]   
   for j in range(n):      
      b.append(int(input()))   
   a.append(b) 
for i in range(n):   
   for j in range(n):   
      print(a[i][j], end = " ")   
   print()        
printDiagonalSums(a, n)