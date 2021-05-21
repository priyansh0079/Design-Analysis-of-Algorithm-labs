import time
def selectionsort(arr):
    start=time.time()
    i=0
    while i<len(arr)-1:
        temp=arr[i]
        c=min(arr[i+1::])
        if c<arr[i]:
            arr[arr.index(min(arr[i::]))]=temp
            arr[i] = c
        i+=1
    end=time.time()

    return (end-start)


def bubblesort(arr):
    #n^2,n,1
    start=time.time()
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                # print(arr)
            else:
                pass
    end=time.time()
    return end-start
def insertionsort(arr):                      #n^2
    start=time.time()
    for i in range(1,len(arr)):
        key=arr[i]
        count=i-1
        for j in range(i-1,-1,-1):
            if arr[j]>key:
                arr[j+1]=arr[j]
                count-=1
        arr[count+1]=key
    end=time.time()
    return end-start

def quicksort(arr,low,high):
    start=time.time()
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
    end=time.time()
    return end-start


def mergesort(arr):          
    start=time.time()
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
    end=time.time()
    return end-start

import random
print("selection sort time complexities")
arr = random.sample(range(1, 100),10)
r1=selectionsort(arr)
print("for n=10 r1=",r1)

arr = random.sample(range(1, 200),100)
r2=selectionsort(arr)
print("for n=100 r2=",r2)

arr = random.sample(range(1, 2000),1000)
r3=selectionsort(arr)
print("for n=1000 r3=",r3)

arr = random.sample(range(1, 20000),10000)
r4=selectionsort(arr)
print("for n=10000 r4=",r4)


print()


print("Bubble sort time complexities")
arr = random.sample(range(1, 100),10)
b1=bubblesort(arr)
print("for n=10 b1=",b1)
arr = random.sample(range(1, 200),100)
b2=bubblesort(arr)
print("for n=100 b2=",b2)
arr = random.sample(range(1, 2000),1000)
b3=bubblesort(arr)
print("for n=1000 b3=",b3)
arr = random.sample(range(1, 20000),10000)
b4=bubblesort(arr)
print("for n=10000 b4=",b4)


print()



print("insertion sort time complexities")
arr = random.sample(range(1, 100),10)
i1=insertionsort(arr)
print("for n=10 i1=",i1)
arr = random.sample(range(1, 200),100)
i2=insertionsort(arr)
print("for n=100 i2=",i2)
arr = random.sample(range(1, 2000),1000)
i3=insertionsort(arr)
print("for n=1000 i3=",i3)
arr = random.sample(range(1, 20000),10000)
i4=insertionsort(arr)
print("for n=10000 i4=",i4)


print()


print("quick sort time complexities")
arr = random.sample(range(1, 100),10)
q1=quicksort(arr,0,len(arr)-1)
print("for n=10 q1=",q1)

arr = random.sample(range(1, 200),100)
q2=quicksort(arr,0,len(arr)-1)
print("for n=100 q2=",q2)

arr = random.sample(range(1, 2000),1000)
q3=quicksort(arr,0,len(arr)-1)
print("for n=1000 q3=",q3)

arr = random.sample(range(1, 20000),10000)
q4=quicksort(arr,0,len(arr)-1)
print("for n=10000 q4=",q4)

print()

print("merge sort time complexities")
arr = random.sample(range(1, 100),10)
m1=mergesort(arr)
print("for n=10 m1=",m1)

arr = random.sample(range(1, 200),100)
m2=mergesort(arr)
print("for n=100 m2=",m2)

arr = random.sample(range(1, 2000),1000)
m3=mergesort(arr)
print("for n=1000 m3=",m3)

arr = random.sample(range(1, 20000),10000)
m4=mergesort(arr)
print("for n=10000 m4=",m4)

import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import interpolate
x = np.array([10,100,1000,10000])
x_new = np.linspace(10, 10000,300)

y1 = np.array([r1,r2,r3,r4])
r_BSpline = interpolate.make_interp_spline(x, y1)
y1_new = r_BSpline(x_new)
plt.plot(x_new,y1_new)

y2=np.array([b1,b2,b3,b4])
b_BSpline = interpolate.make_interp_spline(x, y2)
y2_new=b_BSpline(x_new)
plt.plot(x_new,y2_new)

y3=np.array([i1,i2,i3,i4])
i_BSpline = interpolate.make_interp_spline(x, y3)
y3_new=i_BSpline(x_new)
plt.plot(x_new,y3_new)

y4=np.array([q1,q2,q3,q4])
plt.plot(x,y4)

y5=np.array([m1,m2,m3,m4])

plt.xlabel('n(length of array)')
plt.ylabel('time complexity ')

plt.title('Graphs for different sorting alg(s)')
plt.show()
