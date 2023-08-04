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
            regex = regex + "[^" + word[pos]
            pos2 = 0
            regappend = ''
            for x in colors:
                pos2 += 1
                if i == 'b':
                    regappend += word[pos2 - 1]
            regex += regappend

            regex+= "]"



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

    list6 = []
    for i in ys:
        for x in list2:
            if i in x and x not in list6:
                list6.append(x)
    if len(ys) == 0:
        return list2



    return list6



#for i in list1:
#    if i[0] == "a" or i[1] == "l" or i[3] == "r":
#        print(i)
#print(len(list1))
word = "alert"
colors = "bbybg"
list2 = shrink(list1, word, colors)
print("list2", list2)
list3 = shrink2(list2, word, colors)
print("list3", list3)
print(len(list3))
letters = []
count = 0
for i in colors:
    count +=1
    if i == "b":
        letters.append(word[count-1])
print(letters)
#TODO take 3 has an error
#TODO grasy letters can be taken out of yellow spaces
def take3(list1, word, colors, letters):
    list2 = list1.copy()
    count = 0
    for i in letters:
        count += 1
        for x in list1:
            if i in x:
                try:
                    list2.remove(x)
                except:
                    pass


    return list2
#list4 = take3(list3, word, colors, letters)
#TODO idk if take3 works at all
list4 = list3.copy()
print("list4", list4)
print(len(list4))

letter_dict = {
'E' :(11.1607,56.88),
'A' :(8.4966,43.31),
'R' :(7.5809,38.64),
'I' :(7.5448,38.45),
'O' :(7.1635,36.51),
'T' :(6.9509,35.43),
'N' :(6.6544,33.92),
'S' :(5.7351,29.23),
'L' :(5.4893,27.98),
'C' :(4.5388,23.13),
'U' :(3.6308,18.51),
'D' :(3.3844,17.25),
'P' :(3.1671,16.14),
'M' :(3.0129,15.36),
'H' :(3.0034,15.31),
'G' :(2.4705,12.59),
'B' :(2.0720,10.56),
'F' :(1.8121,9.24),
'Y' :(1.7779,9.06),
'W' :(1.2899,6.57),
'K' :(1.1016,5.61),
"V" :(1.0074,5.13),
'X' :(0.2902,1.48),
'Z' :(0.2722,1.39),
"J" :(0.1965,1.00),
"Q" :(0.1962,1)}


list5 = []
for i in list4:
    value = 0
    for x in i:
        value += letter_dict[x.upper()][1]
    list5.append((value, i))
list5.sort(reverse=True)
print(list5)
print(len(list5))