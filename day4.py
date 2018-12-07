# THIS ONE WAS REALLY HARD.

#########################################################################################################
# part 1
#########################################################################################################

# 1. read in input
# 2. sort by date and time (i think it's year-mo-day and then time so that at least should be not hideously painful)
# 3. create a dictionary with guard ID and then key values 

# read in input and clean up
inf = [line.rstrip() for line in open("./day4_input.txt")]

inf.sort()

# for each item in the array, if it includes "Guard #" then it is a new guard time
# take: the time period from the next stamp and subtract current stamp - can subtract directly (ex. :25 - :05 is 20 min)
# for each line: if it says guard, then set guardID to new ID 
# if it says "falls asleep" that is sleep time
# if it says "wakes up" that is awake time and total sleep is awake - sleep
# update key accordingly

import re

def getGuardSleep(arr):
    
    arr.sort()

    sleepmin = {}
    sleep = False
    awake = False

    # need to get: guard and time 1

    for item in arr:
        # set the guard to be the most recent guard#
        if "Guard #" in item: 
            guard = re.search("#(.+?) ", item).group(1)
            print(guard)

        # get the first "falls asleep"
        elif "falls asleep" in item:
            sleeptime = int(item[15:17])
            print("sleep: " + str(sleeptime))
            sleep = True

        # get the wakeup
        elif "wakes up" in item:
            awaketime = int(item[15:17])
            print("awake: " + str(awaketime))
            awake = True

        # if we have an awake and true, set time asleep value
        if awake == True and sleep == True:
            sleeptot = awaketime - sleeptime
            awake = False
            sleep = False
            print("time asleep: " + str(sleeptot))

            # add the guard and sleep min to the overall dictionary
            if guard in sleepmin:
                sleepmin[guard] = sleepmin.get(guard) + sleeptot
            else:
                sleepmin[guard] = sleeptot
                
    return sleepmin


getGuardSleep(inf)

## get all days the guard in question was on guard
def getGuardDays(guard,arr):
    dayarr = []
    
    for item in arr:
        if guard in item:
            dayarr.append(item[:18])
              
    return dayarr

getGuardDays('1217',inf)

# i then fixed the days manually. I don't know what I was thinking either.

jankysol = ['[1518-05-03',
 '[1518-05-23',
 '[1518-06-11',
 '[1518-06-23',
 '[1518-06-27',
 '[1518-07-14',
 '[1518-07-30',
 '[1518-08-08',
 '[1518-08-28',
 '[1518-09-15',
 '[1518-09-27',
 '[1518-09-30',
 '[1518-10-08',
 '[1518-10-09',
 '[1518-10-20',
 '[1518-10-26',
 '[1518-11-07']

 def getDays(inarr,basearr):
    guardarr = []
    basearr.sort()
    
    for item in inarr:
        for line in basearr:
            if item in line:
                guardarr.append(line)
                
    return guardarr


getDays(jankysol,inf)

# and then i forgot what a dictionary was and figured out the last part by hand. I DON'T KNOW EITHER!!!!!


#########################################################################################################
# part 2:
#########################################################################################################



guards = ['773','2963', '643', '1129', '101', 
          '811', '449', '1049', '613', '3023', 
          '197', '2297', '353', '2333', '1117',
           '1657', '1217', '2789', '3163', '277']


# read in input and clean up
inf = [line.rstrip() for line in open("./day4_input.txt")]

inf.sort()
# 1. create a dictionary that includes the guard ID, then the guard lines, for every guard

guardobj = {}

for guard in guards:
    guardobj[guard] = []

for guard in guards:
    for item in inf:
        # set the guard to be the most recent guard#
        if "Guard #" in item and guard in item: 
            guardfound = True
        elif "Guard #" in item and guard not in item:
            guardfound = False

        if guardfound == True:
            guardobj[guard].append(item)

# this provides: { guard ID: [guard actions list], guard ID: [guard actions list]}
            

# create an object of minutes asleep - this will be from 0 - 60, and be used to store which minutes each guard spends asleep
minsleep = {}

for i in range(61):
    minsleep[i] = 0

import copy

# okay! now: 
# for every entry in the key, create a NEW dictionary 
# each dictionary is called the name of the guard
# every minute that a guard is asleep will be in the dictionary, 0 - 60 
# each minute that is asleep: add 1 to that value 
sleep = False
awake = False

guardsleepobj = {}

for item in guardobj:
    guardsleep = copy.deepcopy(minsleep)
    
    for event in guardobj[item]:
        print(event)
        if "falls asleep" in event:
            sleeptime = int(event[15:17])
            sleep = True

        # get the wakeup
        elif "wakes up" in event:
            awaketime = int(event[15:17])
            awake = True
        
        # if we have an awake and true, set time asleep value
        if awake == True and sleep == True:
            if item in guardsleepobj:
                for i in range(sleeptime,awaketime):
                    guardsleepobj[item][i] = guardsleepobj[item].get(i) + 1
            else:
                for i in range(sleeptime,awaketime):
                    guardsleep[i] = guardsleep.get(i) + 1

                guardsleepobj[item] = guardsleep
                
            
            awake = False
            sleep = False
                
            
# now for each object, find the maximum minutes asleep

import operator


for item in guardsleepobj:
    print(item)
    print(max(guardsleepobj[item].items(), key=operator.itemgetter(1))[1])

for item in guardsleepobj:
    print(item)
    print(max(guardsleepobj[item].items(), key=operator.itemgetter(1))[0])

    
guardsleepobj["2789"][34]

2789*34

#94826

# AAAAAAA I DID IT