# Create a 2D matrix filled with 0
# For every line of the input, add 1 to every square 

# read in input and clean up
qinput = [line.rstrip() for line in open("./day3_input.txt")]


def cleanInput(arr):
    newarr = []
    
    newarr.extend([line.split("@")[1].strip() for line in arr])
    return newarr


qinput_c = cleanInput(qinput)

# carr - cut array; this is the inputs saying where each slice takes place (coord and area)
# basearr - shirt array; this is the input of usually 0's representing the cloth

def getOverlaps(carr,basearr):
    
    for cut in carr:
        # get the coordinates and the width/height of the cuts
        temp = cut.split(":")[0].split(",")
        temp2 = cut.split(":")[1].split("x")
        

        # get the coordinates
        bigarrcoord = int(temp[1])
        smallarrcoord = int(temp[0])

        # width/height 
        bigarrrange = int(temp2[1])
        smallarrrange = int(temp2[0])

        # mark where the overlaps are happening
        for i in range(bigarrrange):
            for j in range(smallarrrange):
                basearr[bigarrcoord + i][smallarrcoord + j] += 1
                


shirt = [[0 for i in range(1000)] for j in range(1000)] 

getOverlaps(qinput_c,shirt)

def countOverlap(arr):
    counter = 0

    for item in arr:
        for sub in item:
            if sub > 1:
                counter = counter + 1
    return counter

print(countOverlap(shirt))

# for every entry in starter array
# go through shirt
# find those squares
# make sure the squares only have [1] in them


def getSingleCut(carr,basearr):
    
    for cut in carr:
        single = True
        
        # get the coordinates and the width/height of the cuts
        temp = cut.split(":")[0].split(",")
        temp2 = cut.split(":")[1].split("x")
        

        # get the coordinates
        bigarrcoord = int(temp[1])
        smallarrcoord = int(temp[0])

        # width/height 
        bigarrrange = int(temp2[1])
        smallarrrange = int(temp2[0])

        # mark where the overlaps are happening
        for i in range(bigarrrange):
            for j in range(smallarrrange):
                if basearr[bigarrcoord + i][smallarrcoord + j] > 1:
                    single = False
                    
        if single == True:
            return cut



print(getSingleCut(qinput_c,shirt))
