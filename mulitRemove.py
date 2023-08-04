list1 = ['first', 'right', 'great', 'might', 'night', 'light', 'point', 'front', 'built', 'least', 'eight', 'sight', 'fight', 'meant', 'spent', 'coast', 'quiet', 'visit', 'fruit', 'count', 'paint', 'sheet', 'doubt', 'sweet', 'wheat', 'giant', 'ought', 'exact', 'chest', 'event', 'orbit', 'shoot', 'tight', 'burst', 'split', 'digit', 'pilot', 'swept', 'exist', 'trust', 'joint', 'shout', 'habit', 'crust', 'midst', 'print', 'fault', 'swift', 'faint', 'ghost', 'feast', 'limit', 'worst', 'beast', 'treat', 'moist', 'burnt', 'guest', 'sweat', 'upset', 'craft', 'shift', 'input', 'twist', 'crept', 'drift', 'waist', 'frost', 'grant', 'shaft', 'scent', 'draft', 'toast', 'wrist', 'robot', 'dwelt', 'knelt', 'dealt', 'roast', 'chant', 'mount', 'react', 'scout', 'stout', 'trout', 'didst', 'greet', 'crest', 'yeast', 'erect', 'quilt', 'guilt', 'boast', 'tract', 'merit', 'quest', 'stunt', 'spout', 'trait', 'saint', 'gaunt', 'snout', 'pivot', 'yacht', 'comet', 'depot', 'rivet', 'boost', 'theft', 'squat', 'vault', 'exalt', 'cheat', 'debut', 'inlet', 'onset', 'roost', 'idiot', 'unfit', 'scant', 'leapt', 'beset', 'stint', 'erupt', 'strut', 'haunt', 'smelt', 'hoist', 'grunt', 'taunt', 'cadet', 'enact', 'covet', 'tempt', 'exult', 'graft', 'edict', 'inept', 'facet', 'beret', 'spilt', 'carat', 'vomit', 'wrest', 'valet', 'shalt', 'taint', 'brunt', 'scoot', 'eject', 'grist', 'civet', 'karat', 'filet', 'refit', 'jaunt', 'befit', 'egret', 'stilt', 'ingot', 'evict', 'daunt', 'remit', 'cruet', 'joist', 'bigot', 'cubit', 'spelt', 'veldt', 'canst', 'leant', 'whist', 'reset', 'gamut', 'inset', 'rebut', 'tacit', 'hadst', 'beget', 'uncut', 'quint', 'sprit', 'fagot', 'fount', 'petit', 'feint', 'caret', 'bidet', 'shunt', 'splat', 'vaunt', 'islet', 'joust', 'motet', 'skeet', 'ducat', 'beaut', 'divot', 'kaput', 'croft', 'moult', 'tenet', 'begot', 'unset', 'kraut', 'snoot', 'crypt', 'unlit', 'legit', 'tryst', 'donut', 'wurst', 'epact', 'posit', 'fixit', 'debit', 'octet', 'recut', 'twixt', 'grout', 'grift', 'durst', 'owlet', 'deist', 'roust', 'unmet', 'foist', 'tarot', 'heist', 'coset', 'tweet', 'poset', 'duvet', 'goest', 'feist', 'eclat', 'mayst', 'exeat', 'stoat', 'doest', 'groat', 'skint', 'oncet', 'seest', 'sprat', 'dicot', 'pssst', 'fugit', 'whipt', 'didot', 'begat', 'brent', 'inapt', 'weest', 'licit', 'bruit', 'brant', 'davit', 'verst', 'expat', 'shoat', 'unapt', 'buret', 'tacet', 'pipet', 'pffft', 'relet', 'liest', 'eruct', 'dixit', 'revet', 'cruft', 'quoit', 'genet', 'owest', 'delft', 'mulct', 'knout', 'picot', 'diest', 'bract', 'demit', 'unhit', 'etext', 'besot', 'dicut', 'pewit', 'bight', 'prest']
indexes = [4,2]

st = "bago"

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

list1, list2 = remove(list1, indexes)

print("lsit1", list1)
print("list2", list2)

letters = ["a", "l", "r"]

def remove2(list1, list2, letters):
    list3 = []
    count = 0
    for i in list1:
        if any(x in ''.join(i) for x in letters):
            continue
        else:
            list3.append(list2[count])
        count+=1

    return list3

l = remove2(list1, list2, letters)
print(l)