"""
Filename: sortingTest.py

CSCI 665: Homework 1
Problem 5: Merge Sort, Insertion Sort, Bucket Sort.

Aditya Ajit Tirakannavar (at2650)
"""

# import statmenets are below

import random
import math
import time

"""
Merge Sort:

This algorithm was taught in CSCI 605 : Computational Problem Solving (Fall 2021) and utilizes the same algorithm.
Credits : Professor Maria Cepeda.

Algorithm Analysis:

Basic Idea: Recursively splits the input list into two halves and goes on splitting until the all the newly generated lists are sorted.
Follows a Divide and Conquer approch.

Divide: Divides the list until its sorted (has only one element).
Conquer: Combine all sorted lists together to form a single sorted list.

Base Case: A list is considered to be sorted if the length of the list is equal to 1.
Recursive Case: The list consists more than one element.

Once the two halves are sorted, we perform the merge step. Merge step combines the two sorted lists into one sorted list.

Time Complexity Analysis:

Time Complexity : O(n * log n)

T(n) = 
MergeSort(X, n):
Base Condition if n(length of array A) == 1, then return X (Sorted Array) - O(1)
Calculate the middleIndex = len(A) // 2 using formula - O(1)
Use the middleIndex to split the array into two halves 
A = X[0: middle - 1] - O(n)
B = X[middle: n] - O(n)
As = MergeSort[A, middle] - T(n/2)
Bs = MergeSort[B, n- middle] - T(n/2)
return Merge(As, Bs) - O(n)

T(n) = O(n) + 2 * T(n/2)
T(n) = O(n * log n)

"""


def mergeSort(aList: list):
    """
    The recursive mergeSort function that splits the list into two halves recurrsively until all the newly generated lists are sorted (length == 1),
    and then merges all sorted lists to form a single sorted list.
    :param aList: Single unsorted list
    :return: Single sorted list
    """

    # Base Condition
    if len(aList) == 1:
        return aList

    # Recursive Condition

    # Calculate middle index to split list into two halves
    midIndex = len(aList) // 2

    # Recursively splits the list until, each new generated list is sorted
    first = mergeSort(aList[0:midIndex])
    second = mergeSort(aList[midIndex:len(aList)])

    # to store the final sorted array
    ans = []
    firstIndex = 0
    secondIndex = 0

    # while there are still elements to compare in the first list and while there are still elements to compare in the second list
    while firstIndex < len(first) and secondIndex < len(second):
        # if element in first list is smaller than element in the second list
        if first[firstIndex] < second[secondIndex]:
            # add that element in the first list
            ans.append(first[firstIndex])
            # increment the index of the first list
            firstIndex += 1

        else:
            # if element in first list is not smaller than element in the second list
            # add the element in the second list
            ans.append(second[secondIndex])
            # increment the index of the second list
            secondIndex += 1

    # adds remainder of the other list
    if firstIndex < len(first):
        # if index of first list is less than length of the first list
        # adds the remainder of the first list to the answer
        ans.extend(first[firstIndex:])

    else:
        # adds remainder of the second list to the answer
        ans.extend(second[secondIndex:])

    # returns the entire sorted list
    return ans


"""
Insertion Sort:

Algorithm Analysis:

Basic Idea: Comapre key with values at previousIndex.

For n-1 iteration:

Do (In every iterations)

As long as previousIndex is greater than or equal to Zero 
AND
the value of key is less than the value at the previousIndex: 

Copy the value (larger value in this case) at previousIndex to location previousIndex + 1.
Decrement the previousIndex by 1.

Check for while loop condition again, and keep moving larger values by one position.

Once the loop reaches and index = 0 or or an index where key value is greater than
the previous value, copy the key value at that location

Repeat the above steps for n-1 iterations.

After completion of all (n-1) iterations, the input array will be sorted in ascending
order.

Time Complexity : O(n^2)

"""


# array of size n
def insertionSort(array):
    # Index position 1 to Index position (n-1)
    for index in range(1, len(array)):
        # Make the element at current index position as Key
        key = array[index]
        # Make the previousIndex value as (current index-1)
        previousIndex = index - 1

        # Checks if the key value is less than value at previousIndex (Index's) and based on results keeps moving
        # larger value one position to the right
        while previousIndex >= 0 and key < array[previousIndex]:
            array[previousIndex + 1] = array[previousIndex]
            previousIndex = previousIndex - 1

        # Finally, puts the small value at the appropriate location.
        array[previousIndex + 1] = key

    return array


"""
Bucket Sort:

Algorithm Analysis:

Basic Idea: Divide the input (uniformly distributed) values into array of size of input
where each input array location is a linked list.

Each array location can be called as a bucket which holds data in a particular range,
say for input values in range [0, 1) and 8 input values,
there will be 8 locations in the array where,
index_0 holds data in range 0 - 0.125
index_1 holds data in range 0.125 - 0.250 and so on. 

Time Complexity : Expected Run time: O(n)

Since the input elements n are uniformly distributed, as per mathametical analysis, the input will be distibuted 
even in the given range [0, k). There we will roughly have equal number of input values in
each bucket, where we have created n buckets for n input values. 
So for truely uniform data, we will get roughly one input value in each bucket we created.

Now, independent of the sorting algorithm we use, we are guaranted we will have a constant number of
input value(s) in each bucket which can be sorted in constant time.

Best Case: O(n)
Each linked list takes ends up with a single element and insertion sort takes constant time per list.
Total cost of insertion sort is Theta(n)

Worst Case: O(n^2)
All elements end up in a singe list and insertion sort takes O(n^2) to sort all elements.

"""


def bucketSort(inputList):
    # length = length of the input array
    length = len(inputList)
    # auxiliary array of length same as input array where each array index is a linked list
    auxArray = []

    # allocate aux array of size 'length' and initalize every index location of array as an empty linked list.
    for index in range(length):
        auxArray.append([])

    # calculate the location where the data in the array will be copied to based on the formula
    # Floor ( length_of_input_array * data )
    for index2 in range(0, length):
        auxArray[math.floor(length * inputList[index2])].append(inputList[index2])
        # Using append operation ensures that the sorting is stable.
        # If the linked list at a specified location is empty, then the append operation works actually as a prepend operation and
        # adds the element at the first available position of the linked list.

    # run insertion sort on each individual linked list and store the sorted list in the same location
    for index3 in range(length):
        auxArray[index3] = insertionSort(auxArray[index3])

    # copy each sorted linked list to the respective inputList location
    k = 0
    for i in range(length):
        for j in range(len(auxArray[i])):
            # copying sorted linked list at location [i] element by element [j] into inputList[k]
            inputList[k] = auxArray[i][j]
            # increment inputList index k by 1
            k += 1
    # returns the sorted inputList
    return inputList


def uniformTestCase():
    # Uniform Distribution Test Case

    """
    Returns a list with data uniformly distributed.
    :param: None
    :return: Uniform unsorted list
    """

    myUniformList = []
    inputVal1 = int(input('Enter the amount of numbers to be sorted: (Uniform Distribution) :'))
    for index1 in range(0, inputVal1):
        x = random.uniform(0, 1)
        myUniformList.append(x)
    return myUniformList


def gaussianTestCase():
    # Gaussian Distribution Test Case

    """
    Returns a list with data gaussian distributed.
    :param: None
    :return: Gaussian unsorted list
    """

    myGaussianList = []
    inputVal2 = int(input('Enter the amount of numbers to be sorted: (Gaussian Distribution) :'))
    for index1 in range(0, inputVal2):
        y = random.gauss(0.5, 0.0001)
        myGaussianList.append(y)
    return myGaussianList


def sortingTest():
    userSelection = int(
        input('Enter from below options for type of Sorting Algorithm to be tested. (Enter the number only) \n'
              'Option 1: Merge Sort \n'
              'Option 2: Insertion Sort \n'
              'Option 3: Bucket Sort \n'))

    if userSelection == 1:

        # To see time analysis as output run the below code
        # start1 = time.time()
        # mergeSort(uniformTestCase())
        # end1 = time.time()
        # print('Time : ', end1 - start1)
        # start2 = time.time()
        # mergeSort(gaussianTestCase())
        # end2 = time.time()
        # print('Time : ', end2 - start2)

        # To see sorted array as output run the below code
        print(mergeSort(uniformTestCase()))
        print(mergeSort(gaussianTestCase()))

    elif userSelection == 2:

        # To see time analysis as output run the below code
        # start1 = time.time()
        # insertionSort(uniformTestCase())
        # end1 = time.time()
        # print('Time : ', end1 - start1)
        # start2 = time.time()
        # insertionSort(gaussianTestCase())
        # end2 = time.time()
        # print('Time : ', end2 - start2)

        # To see sorted array as output run the below code
        print(insertionSort(uniformTestCase()))
        print(insertionSort(gaussianTestCase()))

    elif userSelection == 3:

        # To see time analysis as output run the below code
        # start1 = time.time()
        # print(bucketSort(uniformTestCase()))
        # end1 = time.time()
        # print('Time : ', end1 - start1)
        # start2 = time.time()
        # print(bucketSort(gaussianTestCase()))
        # end2 = time.time()
        # print('Time : ', end2 - start2)

        # To see sorted array as output run the below code
        print(bucketSort(uniformTestCase()))
        print(bucketSort(gaussianTestCase()))


if __name__ == '__main__':
    sortingTest()
