distance = 950
tank = 400
stops = [200, 375, 550, 750]
def min_refills(distance, tank, stops):
    #gasLeft will be used to track whether we can make it to first stop 
    #initialize it to the tank because this is as far we can go. Each 
    #time we fill up we will reset it to the tank 
    gasLeft = tank
    numberFills= 0 
    distance2 = 0 
    #distance will be part of a while loop until we hit the distance than the
    #loop should continue
    count = 1
    #count variable will be used to check condition of the next gas stop
    #basically can you make it to the next staion
    while distance2 < distance:
        for i in stops: 
            gasLeft -= i
            distance2 = i
            #subtracting the distance 
            if distance<tank:
                distance2 = distance
                numberFills=0
                break
            #taking care of condition of tank being enought to get you to 
            #last stop
            elif count == len(stops):
                if (distance - i) > tank: 
                    numberFills = -1
                    distance2= distance
                    break
                elif gasLeft < distance - distance2: 
                    numberFills = numberFills + 1
                    distance2= distance
                else: 
                    distance2 = distance
            elif (stops[count]-i)>tank:
                distance2=distance
                numberFills=-1
                break
            elif gasLeft == 0: 
                gasLeft = tank +i 
                numberFills= numberFills+1  
            #this condition checks for the last station
            elif (stops[count]-distance2)>gasLeft and numberFills !=-1:
                gasLeft= tank + i 
                numberFills =numberFills + 1 
            else: 
                gasLeft = tank
            count+=1
    print(numberFills)
min_refills(distance, tank, stops)

        


    

