from heapq import *


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
    print('Average seek time:  ')
    avg_seek_time = total/len(requests)
    print(avg_seek_time)





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

def C_SCAN(hp,maxPoint):
    req = requests.copy()
    n=len(req)

    req.append(0)
    req.append(maxPoint-1)
    req.append(hp)

    req.sort()

    indx=req.index(hp)

    for i in range(indx+1,len(req)):
        print(str(req[i])+"  seeked")
        
    for i in range(0,indx):
        print(str(req[i])+"  seeked")

    time = 0
    end=maxPoint-1          #end=199
    start=0                 #start=0
    
    time+=abs(end-hp)
    time+=end
    time+=abs(req[indx-1]-start)

    print('total cylinder movement(C-SCAN): ')
    print(time)
	# calculate average seek time
    print('Average seek time:  ')
    avg_seek_time = time/n
    print(avg_seek_time)
    #return avg_seek_time

'''

requests=[98,183,37,122,14,124,65,67]
requests=[82,170,43,140,24,16,190]
head_pointer=53

'''
head_pointer=int(input('Enter the point of head pointer: '))
size=int(input('Enter the size of cylinder: '))
requests=input('Enter the requests: ').split()
for i in range(len(requests)):
    c=int(requests[i])
    requests[i]=c

#driver code
C_SCAN(head_pointer,size)
#sstf(head_pointer,size)
FCFS()



















