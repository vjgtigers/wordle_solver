import os

x = os.walk("./answers2")
x = list(x)
all = []
for i in x[0][2]:
    file = open("./answers2/" + i, "r")
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
print(all)
j = open("words.txt", "w")
j.write("word, answers over 6, word value(idk), percent, avarage guesses\n")
for i in all:
    x = ",".join(i)
    x += "\n"
    j.write(x)
j.close()