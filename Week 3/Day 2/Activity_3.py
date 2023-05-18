def exercise1():
    # Exercise 1: Add item 7000 after 6000 in the following Python List
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    for i in list1:
        if type(i) is list:
            for j in i:
                if type(j) is list:
                    j.append(7000)
    print(list1)

def exercise2():
    # Exercise 2: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    add_list = ["h", "i", "j"]
    for i in add_list:
        list1[2][1][2].append(i)
    print(list1)

def exercise3():
    # Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
    list1 = [5, 10, 15, 20, 25, 50, 20]
    list1[list1.index(20)] = 200
    print(list1)

def exercise4():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    while 20 in list1:
        list1.remove(20)
    print(list1)

# exercise1()
# exercise2()
# exercise3()
exercise4()