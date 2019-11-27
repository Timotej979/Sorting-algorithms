import random as rand
import math
from datetime import datetime


# CLASS FOR SORTING ALGORITHMS
class SortingAlgorithms:

    #INSERTION SORT
    def insertionSort(A):
        for i in range(1, len(A)):
            j = i
            var = A[j]
            while j > 0 and var < A[j-1]:
                A[j] = A[j-1]
                j=j-1
            A[j] = var
        return A

    #QUICK SORT(first element as pivot)
    def quickSort(A):
        if len(A) > 1:
            pivot = A[0]
            i = 0
            for j in range(len(A)-1):
                if A[j+1] < pivot:
                    A[j+1], A[i+1] = A[i+1], A[j+1]
                    i+=1
            A[0], A[i] = A[i], A[0]
            low = SortingAlgorithms.quickSort(A[:i])
            high = SortingAlgorithms.quickSort(A[i+1:])
            low.append(A[i])
            return low + high
        else:
            return A

    #MERGE SORT
    def mergeSort(A):
        if len(A) < 2:
            return A
        else:
            mid = len(A)//2
            l = A[:mid]
            r = A[mid:]
            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    A[k] = l[i]
                    i+=1
                else:
                    A[k] = r[j]
                    j+=1
                k+=1
            while i < len(l):
                A[k] = l[i]
                i+=1
                k+=1
            while j < len(r):
                A[k] = r[j]
                j+=1
                k+=1
            return A


    #HEAP SORT
    def heapConversion(A, index, hsize):
        high = index
        lindex = 2 * index + 1
        rindex = 2 * index + 2
        if lindex < hsize and A[lindex] > A[high]:
            high = lindex
        if rindex < hsize and A[rindex] > A[high]:
            high = rindex
        if high != index:
            A[high], A[index] = A[index], A[high]
            SortingAlgorithms.heapConversion(A, high, hsize)

    def heapSort(A):
        l = len(A)
        for i in range(l//2 -1, -1, -1):
            SortingAlgorithms.heapConversion(A, i, l)
        for i in range(l - 1, 0, -1):
            A[0], A[i] = A[i], A[0]
            SortingAlgorithms.heapConversion(A, 0, i)
        return A


#RANDOM ARRAY GENERATOR
array = [0] * rand.randint(1, 4000)

print("Length of list is {} elements".format(len(array)))

for i in range(0, len(array)-1):
    array[i] = rand.random() * math.exp(rand.randint(-10, 10))

print("Generated list is {}".format(str(array)))


start = datetime.now()
insertion = SortingAlgorithms.insertionSort(array)
delta_i = datetime.now() - start

start = datetime.now()
quick = SortingAlgorithms.quickSort(array)
delta_q = datetime.now() - start

start = datetime.now()
merge = SortingAlgorithms.mergeSort(array)
delta_m = datetime.now() - start

start = datetime.now()
heap = SortingAlgorithms.heapSort(array)
delta_h = datetime.now() - start

if ((insertion == quick) and (quick == merge) and (merge ==heap)):
    print("Insertion sort took {} time.\nQuick sort took {} time.\nMerge sort took {} time.\nHeap sort took {} time.".format(delta_i, delta_q, delta_m, delta_h))



