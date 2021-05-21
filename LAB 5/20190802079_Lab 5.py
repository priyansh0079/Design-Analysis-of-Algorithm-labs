#------------------------------------Finding nth element of fibonacci series----------------------------------------#

#-------------------------------------Using Brute force approach------------------------------------------------#
count=0
def brute_force_fibo(N):
    global count
    if N<=2:
        count+=1
        return 1
    else:
        f= brute_force_fibo(N-1) + brute_force_fibo(N-2)
        count+=1
    return f

p=int(input("Enter N: "))
print("Nth element of fibonacci series using brute force appropach-->",brute_force_fibo(p))
print("Count = ",count)
#------------------------------------Using top bottom approach------------------------------------------------------#


memory={}
count=0
def top_bottom(n,memory):
    global count
    if n in memory:
        return memory[n]
    if n<=2:
        f=1
        count+=1
    else:
        f=top_bottom(n-1,memory)+top_bottom(n-2,memory)
        count+=1
    memory[n]=f
    return f

print()
p=int(input("Enter N: "))
print("Nth element of fibonacci series using top bottom approach-->",top_bottom(p,memory))
print("count = ",count)
print()

#----------------------------------------using bottom top approach--------------------------------------------------------------#

def bottom_top(N):
    n1 = 1
    n2 = 1
    print("Nth element of fibonacci series using bottom top approach-->", end=" ")
    while (N - 2) != 0:
        temp = n1
        n1 = n2
        n2 = n2 + temp
        N -= 1
    return n2

N = int(input("Enter N: "))
print(bottom_top(N))
print()

#------------------------------------------Finding LCS----------------------------------------------------------------#
def LCS(L,A, B, x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif A[i-1]== B[j - 1]:
                L[i][j]=L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index=L[x][y]

    lcs = [""] * (index + 1)
    lcs[index] = ""

    i = x
    j = y
    while i > 0 and j > 0:
        if A[i-1]==B[j-1]:
            lcs[index-1]=A[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i-= 1
        else:
            j-= 1

    print("LCS of "+A+" and "+B+" is "+"".join(lcs))

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

L = [[0 for i in range(len(str2)+1)] for c in range(len(str1) + 1)]
LCS(L,str1, str2, len(str1), len(str2))




