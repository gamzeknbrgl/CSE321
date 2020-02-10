# QUESTION 1
# Function that makes a black,white,black,white... pattern from
# given n black and n white boxes
def blackWhiteBoxPattern(array, left, right):
    # repeat it until there is no middle boxes
    if (left >= right or left == 0):
        return
    else:
        # swap the black and white boxes
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        blackWhiteBoxPattern(array, left + 2, right - 2)

# QUESTION 2
# Function that finds the fake coin in an array
def findFakeCoin(arr, i, l):
    l = int(l)
    arr2 = [None] * (l + 1)
    j = int(i)
    while j != l + 1:
        arr2[j] = j
        j = j + 1
    j = j - 1
    # base case, return the lightweight coin if there any, else return none
    if int(i) == l - 1:
        i = int(i)
        if arr[i] == arr[j]:
            return
        elif arr[i] > arr[l]:
            return arr2[l]
        else:
            return arr2[i]
    else:
        # Even number of coins
        if (l - i + 1) % 2 == 0:
            i = int(i)
            # if left weight > right weight
            if weighbridge(arr, i, ((l + i) // 2) + 1) >= weighbridge(arr, (((l + i) // 2) + 1), l + 1):
                # process the lightweight part
                return findFakeCoin(arr, ((l + i) // 2) + 1, l)
            else:  # if right weight > left weight
                return findFakeCoin(arr, i, (l + i) // 2 + 1)
        # Odd number of coins
        else:
            # if left weight > right weight
            if weighbridge(arr, i, (l + i) // 2) >= weighbridge(arr, ((l + i) // 2), l):
                # process the lightweight part
                return findFakeCoin(arr, ((l + i) // 2), l)
            else:
                # for the middle of array
                arr[(l + i) // 2] = arr[l]
                arr2[(l + i) // 2] = arr2[l]
                return findFakeCoin(arr, i, (l + i) // 2)
# Helper function for fake coin problem,
# calculates the sum of coins
def weighbridge(A, start, end):
    j = int(start)
    sum = 0
    while (j != end):
        sum = sum + A[j]
        j = j + 1
    return sum

# QUESTION 3
# Implementation of quicksort
def quickSort(arr, lo, hi):
  i = lo
  j = hi
  swapCount = 0
  opCount = 0
  pivot = arr[(lo + hi) // 2]
  while i <= j:
    while arr[i] < pivot:
      i += 1
    while pivot < arr[j]:
      j -= 1
    if i <= j:
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      swapCount += 1
      i += 1
      j -= 1
    opCount += 1
  if i < hi:
    swapCount2, opCount2 = quickSort(arr, i, hi)
    swapCount += swapCount2
    opCount += opCount2
  if lo < j:
      swapCount2, opCount2 = quickSort(arr, lo, j)
      swapCount += swapCount2
      opCount += opCount2

  return (swapCount, opCount)
# Implementation of insertion sort
def insertionSort(arr):
    swapcount=0
    opcount=0
    for i in range(1, len(arr)):
        v = arr[i]
        j = i - 1
        while j >= 0 and v < arr[j]:
            swapcount=swapcount+1
            opcount=opcount+1
            arr[j + 1] = arr[j]
            j = j-1
            arr[j + 1] = v
    return swapcount, opcount

#QUESTION 4
# I used the pseudocode from our notebook for this algorithm
def lomutoPartition(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[r]
    array[r] = temp
    return i + 1
# I used the pseudocode from our notebook for this algorithm
# Finds the kth smallest element in a list with positioning
# given list around some value p. We get this value "p" from lomuto partitioning.
def quickselect(a, k):
    l = 0
    r = len(a) - 1
    split_point = lomutoPartition(a, l, r)
    if split_point == r - k + 1:
        result = a[split_point]
    elif split_point > r - k + 1:
        result = quickselect(a[:split_point], k - (r - split_point + 1))
    else:
        result = quickselect(a[split_point + 1:r + 1], k)
    return result
# Finds the median of an array with quickselect function
def findMedian(array):
    n=len(array)
    if n%2==0:
        return (quickselect(array,n//2+1)+ quickselect(array,n//2))/2
    else:
        return quickselect(array,(n//2)+1)

# Driver Function
def main():
    # Question 1
    print("Test of -Question 1-")
    array = ['B', 'B', 'B', 'B', 'B', 'W', 'W', 'W', 'W', 'W']
    print("Array is:")
    print(array)
    print("After:")
    blackWhiteBoxPattern(array, 1, 8)
    print(array)
    array2 = ['B', 'B', 'W', 'W']
    print("Array is:")
    print(array2)
    print("After:")
    blackWhiteBoxPattern(array2, 1, 2)
    print(array2)
    # ------------------------------------------------------------------ #
    # Question2
    print("\nTest of -Question 2-")
    a = [5, 2, 5, 5]
    print("Array is:")
    print(a)
    print("Fake coin is in the", findFakeCoin(a, 0, 3), "th index of array")
    b = [10, 10, 10, 10, 10, 10, 9]
    print("Array is:")
    print(b)
    print("Fake coin is in the", findFakeCoin(b, 0, 6), "th index of array")
    c = [9, 9, 9, 5, 9, 9, 9]
    print("Array is:")
    print(c)
    print("Fake coin is in the", findFakeCoin(c, 0, 6), "th index of array")
    d = [4, 4, 4]
    print("Array is:")
    print(d)
    print("Fake coin is in the", findFakeCoin(c, 0, 2), "th index of array")
    # ------------------------------------------------------------------ #
    print("\nTest of -Question 3-")
    a5 = [12, 11, 13, 5, 6]
    print("Input array:")
    print(a5)
    swapCountQS, opCountQS= quickSort(a5, 0, len(a5) -1)
    print("After quick sort:")
    print(a5)
    print("Swap count of quick sort:", swapCountQS)
    print("Operation count of quick sort:", opCountQS)
    a4 = [12, 11, 13, 5, 6]
    print("Input array:")
    print(a4)
    print("After insertion sort:")
    swapCountIS, opCountIS = insertionSort(a4)
    print(a4)
    print("Swap count of insertion sort:", swapCountIS)
    print("Operation count of insertion sort:", opCountIS)

    a15 = [25,21,22,3,4,15,60]
    print("Input array:")
    print(a15)
    swapCountQS2, opCountQS2= quickSort(a15, 0, len(a15) -1)
    print("After quick sort:")
    print(a15)
    print("Swap count of quick sort:", swapCountQS2)
    print("Operation count of quick sort:", opCountQS2)
    a14 = [25,21,22,3,4,15,60]
    print("Input array:")
    print(a14)
    print("After insertion sort:")
    swapCountIS2, opCountIS2 = insertionSort(a14)
    print(a14)
    print("Swap count of insertion sort:", swapCountIS2)
    print("Operation count of insertion sort:", opCountIS2)

    # ------------------------------------------------------------------ #
    print("\nTest of -Question 4-")
    a8=[3,3,1,8,9,7,6]
    print("Input array:")
    print(a8)
    print("Median of the array:",findMedian(a8))
    a9=[1,4,6,8,9,3,2,5]
    print("Input array:")
    print(a9)
    print("Median of the array:",findMedian(a9))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
