#!/usr/bin/python2.6

if __name__=="__main__":
    # read in file, split by comma and remove quotes
    f = open('names.txt')
    data = f.read().split(',')
    names = []
    for name in data:
        names.append(name[1:-1])

    # sort
    names = sorted(names)

    # convert to value
    scores = []
    for i, name in enumerate(names):
        t = 0
        for letter in name:
            t += ord(letter) - 64
        scores.append(t)
    #print scores[937]
    
    # add them up
    total = 0
    for i, score in enumerate(scores):
        total += (i+1) * score

    print total
