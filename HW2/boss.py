"""
Filename: boss.py

CSCI 665: Homework 2
Problem 4: Micromanager

Authors:
Aditya Ajit Tirakannavar (at2650)
"""

# import statmenets are below

import heapq as hq

time = 0
arrival_time = []
positiveATList = []
flag = False


# finds the indexs where the element is present in the list
def findallindex(ele, aList):
    index_list = []
    for ind_ in range(len(aList)):
        if aList[ind_] == ele:
            index_list.append(ind_)
    return index_list


def performTask(tasks):
    # simulating the tasks until the heap becomes empty

    global time
    global arrival_time

    while len(tasks) > 0:

        # extracting the root task element from the heap having the highest priority and storing it into current task.
        currt = tasks[0]

        #  starting a task by incrementing its run time
        time += 1

        # decrementing from time required to complete for the current task
        currt[2] -= 1

        # decrementing deadline time for all tasks
        for task in tasks:
            task[1] -= 1
            # checking if for any task deadline has passed: if deadline is <= 0 and time required to complete is greater than 0
            if task[1] <= 0 and task[2] > 0:
                return 'NO'

        # popping a task if time required to complete is zero and deadline is greater than or equal to zero
        if currt[2] == 0 and currt[1] >= currt[2]:
            hq.heappop(tasks)

        # finding tasks that have arrival time equal to current global time
        all_ind = findallindex(time, arrival_time)

        for _ind2 in all_ind:
            # converting a min heap into max heap by changing the value of arrival time to neagative.
            positiveATList[_ind2][0] = positiveATList[_ind2][0] * (-1)
            # pushing tasks that have the arrival time equal to current time and simulating the task
            hq.heappush(tasks, positiveATList[_ind2])

    # return yes if all tasks are completed within their individual deadline
    return 'YES'


def main():
    global time
    global positiveATList
    global flag

    # input tasks list
    tasks_heap = []

    # perform heapify operation maintaining the heap balance and heap order property
    hq.heapify(tasks_heap)

    # storing the number of tasks into var
    numOfTasks = int(input())

    for _ind1 in range(0, numOfTasks):

        readList = [int(_ind2) for _ind2 in input().split()]

        # list of arrival time of all tasks
        arrival_time.append(readList[0])

        #  task array
        positiveATList.append(readList)

        while flag is False and time != readList[0]:
            time += readList[0]

        if time == readList[0]:
            # converting a min heap into max heap by changing the value of arrival time to neagative.
            readList[0] = readList[0] * (-1)

            # pushing the element into the heap
            hq.heappush(tasks_heap, readList)
            flag = True

    # invoking perform task function
    print(performTask(tasks_heap))


# main conditional guard
if __name__ == '__main__':
    main()
