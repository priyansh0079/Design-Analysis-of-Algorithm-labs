#-----------------------------------Heap sort----------------------------------------------------------------------#
import random
import time                                  #Code for fourth part is written first
import os                                    #so as to avoid the addition of memory utilized
                                                #by others lines of code.....
def memory():
    import psutil
    process=psutil.Process(os.getpid())
    mem=process.memory_info()[0]/float(2**20)
    return mem

def heapsort(arr,n,i):
    large_element=i
    left=(2*i)+1
    right=(2*i)+2

    if left<n and arr[i]<arr[left]:
        large_element=left
    if right<n and arr[right]>arr[large_element]:
        large_element=right
    if i!=large_element:
        arr[i],arr[large_element]=arr[large_element],arr[i]

        heapsort(arr,n,large_element)

def HpSrt(arr):
    for j in range(len(arr)//2-1,-1,-1):
        heapsort(arr,len(arr),j)

    for p in range(len(arr)-1,0,-1):
        arr[0],arr[p]=arr[p],arr[0]
        heapsort(arr,p,0)

array=[10,100,500,1000,10000]
T_HS=[]
M_HS=[]
for i in array:
    start=time.time()
    arr = random.sample(range(1,i*10),i)
    end=time.time()
    HpSrt(arr)
    T_HS.append(end-start)
    M_HS.append(memory())

print("Running heap sort.....")
print()
for i in range(len(T_HS)):
    print("For n= ",array[i], "Time=",T_HS[i])
print()
for j in range((len(M_HS))):
    print("For n= ",array[j], "memory-->",M_HS[j])
print()

import matplotlib.pyplot as plt

plt.plot(array,T_HS,label="Heap Sort",marker="*")
plt.title("n Vs runtime graph")
plt.xlabel("length of array")
plt.ylabel("Runtime value")
plt.legend()
plt.show()

plt.plot(array,M_HS,label="Heap Sort",marker="+")
plt.title("n Vs Memory utilization graph")
plt.xlabel("length of array")
plt.ylabel("Memory utilization")
plt.legend()
plt.show()

#----------------------------------Binary search Tree--------------------------------------------------------#

class node():
    def __init__(self,key,left,right):
        self.key=key
        self.left=left
        self.right=right

print("Inserting values in BST.......")
print()

class BST:
    def __init__(self):
        self.root=None

#-----------------------------insertion into binary search tree----------------------------------------------#

    def insert(self,r,value,i):
        Newnode=node(value,None,None)
        if r==None:
            r=self.root
            r=self.root=node(value,None,None)
            print("Node",i,"-->",r.key,"inserted")
            return i+1

        elif r.key<value:

            if r.right==None:
                r.right=Newnode
                print("Node",i,"-->",r.right.key,"inserted")
                return i+1

            else:
                self.insert(r.right,value,i)
                return i+1

        else:

            if r.left==None:
                r.left=Newnode
                print("Node",i,"-->",r.left.key,"inserted")
                return i+1

            else:
                self.insert(r.left,value,i)
                return i+1


#----------------------------Code to extract numbers from text file---------------------------------------------#

file=open('numbers.txt')
array = []
for line in file.readlines():
    array.append (int(line.rstrip()))

#------------------------------------inserting numbers into tree--------------------------------------------------#

i=1
L=BST()
for j in range(len(array)):
    i=L.insert(L.root,array[j],i)


print()

#-----------------------------inorder display of the binary search tree--------------------------------------------#

print("In order traversel-->",end=" ")
def printInorder(root):
    if root:
        printInorder(root.left)

        print(root.key,end=", ")

        printInorder(root.right)

printInorder(L.root)
print()
print()
#---------------------------------------------Max depth function--------------------------------------------------#
def maxDepth(r):
    if r==None:
        return 0
    else:
        leftDepth = maxDepth(r.left)
        rightDepth = maxDepth(r.right)
        if (leftDepth > rightDepth):
            return leftDepth + 1
        else:
            return rightDepth + 1

result1=maxDepth(L.root)
print("The max depth for the BST= ",result1)
#------------------------------------------Min depth function-------------------------------------------------------------#

def minDepth(r):
    if r is None:
        return 0
    if r.left==None and r.right==None:
        return 1

    if r.left==None:
        return minDepth(r.right)+1

    if r.right==None:
        return minDepth(r.left)+1

    return min(minDepth(r.left), minDepth(r.right))+1

Result2=minDepth(L.root)
print("The min depth for the BST= ",Result2)
print()
#---------------------------------Lowest common ancestor function----------------------------------------------------#

def LCA(r,i,j):
    if r==None:
        return None
    if r.key>i and r.key>j:
        return LCA(r.left,i,j)
    elif r.key<i and r.key<j:
        return LCA(r.right,i,j)
    else:
        return r.key

print("Enter any two nodes of BST in order to find LCA")
i=int(input("Enter first node: "))
j=int(input("Enter second node: "))

lca=LCA(L.root,i,j)
print("The LCA of ",i," and ",j," is ",lca)




