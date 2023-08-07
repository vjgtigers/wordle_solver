import os

x = os.walk("./answers")
x = list(x)
all = []
for i in x[0][2]:
    file = open("./answers/" + i, "r")
    d = file.readlines()

    for p in d:
        p = p.strip("\n")

        p = p.split(" ")

        list1 = []
        for r in p:
            if r != '':
                list1.append(r)
        all.append(list1)
print(len(all))


all.sort(key=lambda x:x[1])
print(all[0])