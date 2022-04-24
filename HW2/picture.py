"""
File Name:  picture.py
Author:     Aditya Ajit Tirakannavar (at2650@rit.edu)
Course:     CSCI-665 Foundations of Algorithms
HW 2.5:     Write a program that finds the number of swaps required to get people in the
            specified order of their age and height
            The first line of the input will be the total # people.
            This will be followed by n input lines,
            each line containing 2 numbers which are age and height in cm.
"""


def divide_step(people):
    '''
    The function will recursively divide the list until it reaches the base case into half
    which takes complexity of O(logn) and n people iterated log(n) times gives O(n log(n)).
    @:param : people : List of students and Teacher
    @:return : merge, swaps: merged list and swap count
    '''

    swaps = 0
    # base case
    if len(people) <=1:
        return people,swaps
    #recursive call
    right, right_swaps = divide_step(people[len(people) // 2:])
    left, left_swaps = divide_step(people[:len(people) // 2])

    #recusive call for the conquer step
    merge, swaps = conquer_step(left, right)
    #counting all the swaps of recursive calls
    swaps += (left_swaps + right_swaps)

    return merge,swaps

def conquer_step(left, right):
    '''
    This Method merges left half and right half of the list based on some conditions
    If both left and right element is a student of 7 year
    we sort according to ascending order of height.
    If both left and right element is a student of 8 year
    we sort according to descending order of height.
    If left is 7 year student and right is 8 year
    then 7 year student will have the preference.
    If left is 7 or 8 year student and right is Teacher
    then 7 or 8 year student will have the preference.
    While merging swap count is counted using counting inversion.
    Overall Complexity turns out to be O(n*logn)

    @:param: left : leftside of half
    @:param: right : rightside of half
    @:return: merged list of left half and right half and swap count
    '''

    result = list()
    #index pointers to compare elements and swaps to store swap count
    left_ind,right_ind,swaps = 0,0,0

    #compares the value and merges the element
    while left_ind < len(left) and right_ind < len(right):
    #left element and right element is 7 compare according to their height
        if left[left_ind][0] == 7 and right[right_ind][0] == 7:
            #compare height if left element has less height add it to the result
            if left[left_ind][1] < right[right_ind][1]:
                result.append(left[left_ind])
                # increment left index
                left_ind +=1
            # if height of left element is greater than or equal to right element
            else:
                # increment swap count by number of swap required by the index value to reach its actual position
                swaps += (len(left) - left_ind)
                result.append(right[right_ind])
                # increment right index
                right_ind+=1

    # left element right element = 8 comapre according to height
        elif left[left_ind][0] == 8 and right[right_ind][0] == 8:
            #compare height
            if left[left_ind][1] < right[right_ind][1]:
                swaps += len(left) - left_ind
                result.append(right[right_ind])
                # increment right index
                right_ind +=1
            else:
                result.append(left[left_ind])
                # increment left index
                left_ind+=1
    # left list's element is a teacher (if age is greater than 8) compare right element
        elif left[left_ind][0] > 8  :
            #right element = 7 append 7 to result
            if right[right_ind][0] == 7:
                # increment swap count
                swaps += len(left) - left_ind
                result.append(right[right_ind])
                # increment right index
                right_ind+=1
            #right element = 8 append teacher
            else:
                result.append(left[left_ind])
                # increment left index
                left_ind += 1
    #right list's element is teacher (if age is greater than 8) compare left element
        elif right[right_ind][0] > 8  :
            #if left = 7 append student
            if left[left_ind][0] == 7:
                result.append(left[left_ind])
                # increment left index
                left_ind+=1
            #else left = 8 append teacher
            else:
                swaps += len(left) - left_ind
                result.append(right[right_ind])
                # increment right index
                right_ind += 1

    #if both left and right are different i.e 7 year and 8 year
    #student comparison will append 7 year student.
        elif left[left_ind][0] < right[right_ind][0]:
            result.append(left[left_ind])
            # increment left index
            left_ind+=1
        else:
            swaps += len(left) - left_ind
            result.append(right[right_ind])
            # increment right index
            right_ind+=1


    #Append the remaining element to the result
    if left_ind < len(left):
        result.extend(left[left_ind:])
    elif right_ind < len(right):
        result.extend(right[right_ind:])

    return result,swaps


def main():
    # total class strength including teacher
    total_people = int(input().strip())
    # list to store age and height
    people = list()
    # input age and height
    if total_people <= 1000:
        for _ in range(total_people):
            age, height = [i for i in input().strip().split(" ")]
            if int(age) <=100:
                people.append([int(age), float(height)])
            else:
                exit()
        sorted_list, swaps = divide_step(people)
        print(swaps)
    else:
        exit()

if __name__ == '__main__':
    main()
