
# open the input
alist = [l.rstrip() for l in open("./day2_input.txt")]

# check for 3 repeats and 2 repeats
def getCheckSum(arr):
    twoarr = []
    threearr = []
    
    for word in arr:
        letterarr = []
        doubletwo = False
        doublethree = False
    
        for y in word:
            if y not in letterarr:
                letterarr.append(y)
                if word.count(y) == 3:
                    doublethree = True
                elif word.count(y) == 2:
                    doubletwo = True
        if doubletwo == True:
            twoarr.append(word)

        if doublethree == True:
            threearr.append(word)
    
    return(len(threearr)*len(twoarr))

# calculate
print(getCheckSum(alist))