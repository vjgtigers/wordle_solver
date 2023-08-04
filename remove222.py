x = ['great', 'least', 'eight', 'meant', 'spent', 'quiet', 'sheet', 'sweet', 'wheat', 'exact', 'chest', 'event', 'swept', 'exist', 'feast', 'beast', 'treat', 'guest', 'sweat', 'upset', 'crept', 'scent', 'dwelt', 'knelt', 'dealt', 'react', 'greet', 'crest', 'yeast', 'erect', 'merit', 'quest', 'comet', 'depot', 'rivet', 'theft', 'exalt', 'cheat', 'debut', 'inlet', 'onset', 'leapt', 'beset', 'erupt', 'smelt', 'cadet', 'enact', 'covet', 'tempt', 'exult', 'edict', 'inept', 'facet', 'beret', 'wrest', 'valet', 'eject', 'civet', 'filet', 'refit', 'befit', 'egret', 'evict', 'remit', 'cruet', 'spelt', 'veldt', 'leant', 'reset', 'inset', 'rebut', 'beget', 'petit', 'feint', 'caret', 'bidet', 'islet', 'motet', 'skeet', 'beaut', 'tenet', 'begot', 'unset', 'legit', 'epact', 'debit', 'octet', 'recut', 'owlet', 'deist', 'unmet', 'heist', 'coset', 'tweet', 'poset', 'duvet', 'goest', 'feist', 'eclat', 'exeat', 'doest', 'oncet', 'seest', 'begat', 'brent', 'weest', 'verst', 'expat', 'buret', 'tacet', 'pipet', 'relet', 'liest', 'eruct', 'revet', 'genet', 'owest', 'delft', 'diest', 'demit', 'etext', 'besot', 'pewit', 'prest']
indexes = [4,2]
letters = ["a", "l", "r"]
def remove(list1, indexes):
    list2 = list1.copy()
    for e in indexes:
        count = 0
        for i in list1:
            i = list(i)

            del i[e]
            list1[count] = i
            count +=1
    return list1, list2

list1, list2 = remove(x, indexes)

print("lsit1", list1)
print("list2", list2)
#TODO not working because its not checking the 2 index for invalid answers


#count = 0
#final = []
#for i in list1:
#    if any(x in i for x in letters):
#        continue
#    else:
#        print(list2[count])
#        final.append(list2[count])
#    count +=1
#print(final)
#print(len(final))

list3 = list2.copy()
count = 0
for i in list1:
    count +=1
    for x in letters:
        #print(x)
        #print("test:", x, i, list2[count-1])
        if x in i:
            #print(i)
            #print(list2[count-1])
            try:
                list3.remove(list2[count-1])
            except:
                pass
print(list3)
print(len(list3))