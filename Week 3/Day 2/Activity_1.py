def exercise1():
    # Exercise 1: Reverse a given list in Python

    aLsit = [100, 200, 300, 400, 500]
    print(aLsit)
    aLsit.reverse()
    print(aLsit)

def exercise2():
    # Exercise 2: Concatenate two lists index-wise

    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]

    print(list1)
    print(list2)
    for i in range(0,4):
        new_list.append(list1[i] + list2[i])
    print(new_list)

def exercise3():
    # Exercise 3: Given a Python list of numbers. Turn every item of a list into its square

    aList = [1, 2, 3, 4, 5, 6, 7]
    bList = []
    for i in aList:
        bList.append(int(i)**2)
    print(aList)
    print(bList)

exercise1()
exercise2()
exercise3()