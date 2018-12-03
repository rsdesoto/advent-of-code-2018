
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

# part 2:
# note: i know this isn't very pythonic. if i wanted to get pythonic with it, i'd use itertools, but i wanted 
# to do this without additional modules. this was a dumb thing to do, but i did it :')

def getSame(arr):
    
    morediff = {} #for testing purposes

    #using indices for the list in order to compare each value to the values following
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            firstdiff = False
            seconddiff = False

            #using the index values for each letter, compare each letter to its equivalent in the next items
            for k in range(len(arr[i])):
                if arr[i][k] != arr[j][k] and firstdiff == False:
                    firstdiff = True
                
                elif arr[i][k] != arr[j][k]:
                    seconddiff = True   

            if seconddiff == True:
                morediff.update({arr[i] : arr[j]}) #for testing purposes
            else:
                return arr[i], arr[j]
    
# compare each item in the 2-part tuple to get the common letters
def compareTup(tup):
    s1 = tup[0]
    s2 = tup[1]
    common = []
    
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            common.append(s1[i])
    
    return ''.join(common)

sameGet = getSame(alist)
print(compareTup(sameGet))