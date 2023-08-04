# This is a sample Python script.
import re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
f = open("C:\\Users\\vjgti\\Downloads\\words5Letters.txt", "r")
list1 = []
e = f.readlines()
for i in e:
    #print(i)
    list1.append(i.replace("\n", ""))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#print(list1)


def shrink(list1, word, colors):
    list22 = []
    regex = '^'
    pos =0
    for i in colors:
        if i == "g":
            regex = regex + "[" + word[pos] + "]"
        if i == "b":
            regex = regex + "[^" + word[pos] + "]"
        if i == "y":
            regex = regex + "."


        pos +=1
    regex = regex + "$"


    for i in list1:
        x = re.findall(regex, i)

        if (x):
            list22.append(i)
        else:
            continue
    return list22

def shrink2(list2, word, colors):
    pos = 0
    indexes = []
    ys = []
    list3 = list2
    list4 = []
    for i in colors:
        if i == "y" or i == "g":
            indexes.append(pos)

        if i == "y":
            ys.append(word[pos])
        pos +=1
    indexes.reverse()
    print(indexes)
    print(list2)

    for i in range(5):
        if i not in indexes:
            print(i)
        else:
            print(i, "in")
    list6 = []
    for i in ys:
        for x in list2:
            if i in x and x not in list6:
                list6.append(x)




    return list6



#for i in list1:
#    if i[0] == "a" or i[1] == "l" or i[3] == "r":
#        print(i)
#print(len(list1))
word = "alert"
colors = "bbybg"
list2 = shrink(list1, word, colors)
if "beget" in list2:
    print(list2.index("beget"))
list3 = shrink2(list2, word, colors)
print(list3)
print(len(list3))
