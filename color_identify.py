o_answer = "alert"
o_guess = "apple"
answer = list(o_answer)
guess = list(o_guess)
answer2 = list(o_answer)
guess2 = list(o_guess)
gs= []
ys = []
for i in list(guess), list(answer):
    print(i)
count = 0
#green loop
for i in guess2:
    count +=1
    if i == answer2[count-1]:
        print(i, count-1)
        gs.append((i, count-1, 'g'))
        guess2[count-1] = "&"
        answer2[count-1] = "*"
count=0
for i in guess2:
    count +=1
    count2 = 0
    for x in answer2:
        count2+=1
        if x == i:
            ys.append((guess[count-1], count-1, 'y'))
            guess2[count - 1] = "&"
            answer2[count2 - 1] = "*"

both = []
for i in ys:
    both.append(i)
for i in gs:
    both.append(i)

print(gs)
print(guess2)
print(answer2)
print(ys)
print(both)
from colorama import Fore, Back, Style
both = sorted(both, key=lambda x: x[1])
print(both)


count = 0
colors = ''
for i in o_guess:
    count+=1
    print1 = False
    lencount = 0
    for x in both:
        lencount +=1
        if count-1==x[1]:
            if x[2] == 'y' and print1 == False:
                print(Fore.YELLOW + i + Style.RESET_ALL, end='')
                colors += 'y'
                print1 = True
            if x[2] == 'g' and print1 == False:
                print(Fore.GREEN + i + Style.RESET_ALL, end='')
                colors += 'g'
                print1 = True
        elif print1 == False and len(both) == lencount:
            print(Fore.BLACK + i + Style.RESET_ALL, end='')
            print1 = True
            colors += 'b'
print()
print(colors)