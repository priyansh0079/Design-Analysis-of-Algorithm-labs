import time
import os
from collections import deque
import random
import psutil

# ---------------------------------recursive quick sort----------------------------------------------------#

def quicksort(arr,low,high):
    def sort(arr, low, high):
        pivot = arr[high]
        j = low
        for i in range(low, high):
            if i == j:
                if arr[i] > pivot:
                    pass
                else:
                    j += 1
            else:
                if arr[i] < pivot:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    j += 1
        arr[j], arr[high] = arr[high], arr[j]
        return j
    if low<high:
        j=sort(arr,low,high)
        quicksort(arr, low, j - 1)
        quicksort(arr, j + 1, high)
    return arr


#----------------------------------------iterative quick sort---------------------------------------------#

def iterativeQuickSort(arr):

    stack = deque()

    start = 0
    end = len(arr) - 1
    stack.append((start, end))

    while stack:
        start, end = stack.pop()
        pivot = arr[end]

        j = start

        for i in range(start, end):
            if arr[i] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                j = j + 1

        arr[j], arr[end] = arr[end], arr[j]

        if j - 1 > start:
            stack.append((start, j - 1))

        if j + 1 < end:
            stack.append((j + 1, end))
    return arr
#---------------------------------------recursive merge sort------------------------------------------------#

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]

        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
    return arr

#  #--------------------------------iterative merge sort------------------------------------------#

def iterativemergeSort(arr):
    size = 1

    while size< len(arr)-1:
        left=0
        while left < len(arr)-1:
            mid = min((left + size - 1), len(arr) - 1)
            right = ((2 * size + left - 1, len(arr) - 1)[2 * size + left - 1 > len(arr) - 1])
            n1 = mid - left + 1
            n2 = right - mid
            L = [0] * n1
            R = [0] * n2
            for i in range(0, n1):
                L[i] = arr[left + i]
            for i in range(0, n2):
                R[i] = arr[mid + i + 1]

            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if L[i] > R[j]:
                    arr[k] = R[j]
                    j += 1
                else:
                    arr[k] = L[i]
                    i += 1
                k += 1

            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

            left = left + size * 2
        size = 2 * size
    return arr

#-----------taking 5 user inputs to calculate run time and memory utilization in each alg.-----------------------------------------#
T_QSR=[]
T_QSI=[]
T_MSR=[]
T_MSI=[]

M_QSR=[]
M_QSI=[]
M_MSR=[]
M_MSI=[]

inp=int(input("Enter no. of inputs to be taken: "))
lst=[]
for i in range(1,inp+1):
    print("enter array length ",i,": ",end="")
    n=int(input())
    lst.append(n)
print()

#------------------------envoking algs--------------------------------------------------------#

for i in lst:
    arr = random.sample(range(1, i*10), i)
    start = time.time()
    process = psutil.Process(os.getpid())
    recursive_quick_sort = quicksort(arr,0,len(arr)-1)                            #invoking
    mem_QS_R=process.memory_info()[0] / float(2 ** 20)
    M_QSR.append((mem_QS_R))
    end = time.time()
    QS_R=end-start
    T_QSR.append(QS_R)

    start = time.perf_counter()
    process = psutil.Process(os.getpid())
    iterative_quick_sort = iterativeQuickSort(arr)
    mem_QS_I = process.memory_info()[0] / float(2 ** 20)
    M_QSI.append(mem_QS_I)
    end = time.perf_counter()
    QS_I = end - start
    T_QSI.append(QS_I)

    start = time.perf_counter()
    process = psutil.Process(os.getpid())
    recursive_merge_sort = mergesort(arr)
    mem_MS_R = process.memory_info()[0] / float(2 ** 20)
    M_MSR.append(mem_MS_R)
    end = time.perf_counter()
    MS_R = end - start
    T_MSR.append(MS_R)

    start = time.time()
    process = psutil.Process(os.getpid())
    iterative_merge_Sort = iterativemergeSort(arr)
    mem_MS_I = process.memory_info()[0] / float(2 ** 20)
    M_MSI.append(mem_MS_I)
    end = time.time()
    MS_I = end - start
    T_MSI.append(MS_I)

def printlst(Tm,Ln,M):
    for i in range(len(Ln)):
       print("for n= ", Ln[i],"t= ",Tm[i]," memory utilization= ",M[i])

printlst(T_QSR,lst,M_QSR)
print()
printlst(T_QSI,lst,M_QSI)
print()
printlst(T_MSR,lst,M_MSR)
print()
printlst(T_MSI,lst,M_MSI)

#-----------------------------------graph for runtime-----------------------------------------------

import matplotlib.pyplot as plt

plt.plot(lst,T_QSR,label="Recursive quick sort",marker="*")
plt.plot(lst,T_QSI,label="iterative quick sort",marker="+")
plt.plot(lst,T_MSR, label="recursive merge sort",marker="^")
plt.plot(lst,T_MSI,label="iterative quick sort",marker="*")
plt.title("n Vs runtime graph")
plt.xlabel("input value")
plt.ylabel("Runtime value")
plt.legend()
plt.show()

#-----------------------------graph for memory utilization----------------------------------------

plt.plot(lst,M_QSR,label="Recursive quick sort",marker="*")
plt.plot(lst,M_QSI,label="iterative quick sort",marker="+")
plt.plot(lst,M_MSR, label="recursive merge sort",marker="^")
plt.plot(lst,M_MSI,label="iterative quick sort",marker="*")
plt.title("n Vs Memory utilization graph")
plt.xlabel("input value")
plt.ylabel("memory value")
plt.legend()
plt.show()

