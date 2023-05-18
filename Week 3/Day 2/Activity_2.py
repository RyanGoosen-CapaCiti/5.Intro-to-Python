def exercise1():
    # Exercise 1: Concatenate two lists in the following order
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    new_list = []
    for i in list1:
        for j in list2:
            new_list.append(i + j)
    print(new_list)

def exercise2():
    # Exercise 2: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    for i in range(4):
        print(list1[i], list2[-i-1])

def exercise3():
    # Exercise 3: Remove empty strings from the list of strings
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    new_list = []
    for x in list1:
        if x != '':
            new_list.append(x)
    print(new_list)

exercise1()
exercise2()
exercise3()