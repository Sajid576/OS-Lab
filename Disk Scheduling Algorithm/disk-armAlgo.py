from heapq import *

requests=[98,183,37,122,14,124,65,67]
#requests=[82,170,43,140,24,16,190]
head_pointer=53

#first come first serve
#here, seek time is relatively high
#performance is relatively low
#but there is no starvation as the requests that are coming 
#into the queue are being processed immediately

def FCFS():
    total=0
    total+=abs(requests[0]-head_pointer)
    for i in range(1,len(requests)):
        total+= abs(requests[i]-requests[i-1])
    print("total cylinder movement(FCFS):  ")
    print(total)





#shortest seek time first(SSTF)
#here,the is to pick a request that is nearest to the r/w
#head pointer

#seek time is relatively low
#performance is much better
#but there is problem of starvation as a request might have to 
#wait too long to being processed

def sstf(hp):
    req = requests.copy()
    time = 0
    position = hp
    n = len(req)
    heap = []
    while len(req) > 0:
        for r in req:
            heappush(heap,(   abs(position - r), r  ) )
        x = heappop(heap)[1]
        time += abs(position - x)
        position = x
        print ('        ', x, '  seeked')
        req.remove(x)
        heap = []

    # calculate average seek time

    avg_seek_time = time / n
    return avg_seek_time

def C_SCAN(hp):
    req = requests.copy()
    n=len(req)
    req.append(hp)
    req.sort()
    indx=req.index(hp)

    for i in range(indx+1,len(req)):
        print(str(req[i])+"  seeked")
    for i in range(0,indx-1):
        print(str(req[i])+"  seeked")

    time = 0
    end=199
    start=0
    
    time+=abs(end-hp)
    time+=end
    time+=abs(req[indx-1]-start)

    print(time)
	# calculate average seek time
    avg_seek_time = time/n
    return avg_seek_time





#C_SCAN(head_pointer)
sstf(head_pointer)
#FCFS()



















