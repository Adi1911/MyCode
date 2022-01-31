def stableMatch_1stGrp(n, first, second):
    unmatched_Elements = list(range(n))
    first_Grp = [None] * len(first)
    second_Grp = [None] * len(second)

    while (unmatched_Elements):
        firstGrp_asker = unmatched_Elements.pop()
        for Second_grp_ele in first[firstGrp_asker]:
            if second_Grp[firstGrp_asker] == None and first_Grp[Second_grp_ele] == None:
                second_Grp[firstGrp_asker] = Second_grp_ele
                first_Grp[Second_grp_ele] = firstGrp_asker
                break
            else:
                currently_matched = first_Grp[Second_grp_ele]
                if (second[Second_grp_ele].index(currently_matched) > second[Second_grp_ele].index(firstGrp_asker)):
                    second_Grp[currently_matched] = None
                    second_Grp[firstGrp_asker] = Second_grp_ele
                    first_Grp[Second_grp_ele] = firstGrp_asker
                    unmatched_Elements.append(currently_matched)
                    break
    return second_Grp


def stableMatch_2ndGrp(n, first, second):
    free_Second_grp_ele = list(range(n))
    first_Grp = [None] * len(first)
    second_Grp = [None] * len(second)

    while (len(free_Second_grp_ele) > 0):
        unmatched_Elements = free_Second_grp_ele.pop()
        for first_grp_ele in second[unmatched_Elements]:

            if first_Grp[unmatched_Elements] == None and second_Grp[first_grp_ele] == None:
                first_Grp[unmatched_Elements] = first_grp_ele
                second_Grp[first_grp_ele] = unmatched_Elements
                break
            else:
                currently_matched = second_Grp[first_grp_ele]
                if (first[first_grp_ele].index(currently_matched) > first[first_grp_ele].index(unmatched_Elements)):
                    first_Grp[currently_matched] = None
                    first_Grp[unmatched_Elements] = first_grp_ele
                    second_Grp[first_grp_ele] = unmatched_Elements
                    free_Second_grp_ele.append(currently_matched)
                    break
    return second_Grp

def main():
    first = []
    second = []
    n = int(input().strip())
    for i in range(n):
        first.append([int(x) for x in input().strip().split(' ')])
    for j in range(n):
        second.append([int(x) for x in input().strip().split(' ')])

    result_first_grp = stableMatch_1stGrp(n,first, second)
    # print(result_first_grp)
    result_Second_grp = stableMatch_2ndGrp(n,first, second)
    # print(result_Second_grp)

    for i in range(n):
        if result_first_grp[i] == result_Second_grp:
            result = 'NO'
        else:
            result = 'YES'
            break
    print(result)


if __name__ == '__main__':
    main()