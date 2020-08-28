# here,elements of refString denotes the page number of the process 
refString=[7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1]

def fifo(n):
    #size of RAM/total number of frames
    
    frameList=[-1]*n
    pageFaultCnt=0

    
    #f denotes the frame index
    f=0
    for i in range(len(refString)):
        if(f%3==0):
            f=0
        if(refString[i] not in frameList):
            frameList[f]=refString[i]
            f+=1
            pageFaultCnt+=1

    print('total page fault:  ')
    print(pageFaultCnt)
    rate=(pageFaultCnt/len(refString))*100
    print(str(rate)+'%')


def findFrameForOptimal(n,refIndx,frameList):
    
    #this list used for keeping track of the target frame
    #  index where replacement will occur
    targetFrameList=[]

    #this var used for setting a frame index highest priority
    # for the replacement.This will occur when a value of
    #a particular frame wont be found after refIndx.

    MAX_PRIOR=1000000
    MaxPriorCounter=0
    print(str(frameList)+"--->"+str(refIndx))
    for i in range(len(frameList)):
        
        try:
            #value is searched after refIndx
            indx=refString.index(frameList[i],refIndx)
            targetFrameList.append((indx,i))
        except ValueError:
            indx=MAX_PRIOR
            targetFrameList.append((indx,i))
            MaxPriorCounter+=1
   
    #if no values in RAM are found in remainging refstring then fifo will be called
    if(MaxPriorCounter==len(frameList)):
        return searchFifo(frameList,refIndx)
    else:
        targetFrameList.sort(key=lambda x: x[0],reverse=True)
        print(targetFrameList[0][1])
        return targetFrameList[0][1]
    
#this function will traverse left side of the refString and find the furthest value 
def searchFifo(frameList,refIndx):
    targetFrameList=[]
    
    for i in range(len(frameList)):
        try:
            #value is searched between 0 and refIndx
            indx=refString.index(frameList[i],0,refIndx)
            targetFrameList.append((indx,i))
        except ValueError:
            pass
    print(len(targetFrameList))
    targetFrameList.sort(key=lambda x: x[0])
    return targetFrameList[0][1]

def OptimalPageRepalce(n):
    # n=size of RAM/total number of frames
    
    frameList=[-1]*n
    pageFaultCnt=0

    #f denotes the frame index
    f=0
    for i in range(0,len(refString)):
        
        if(refString[i] not in frameList):
            #this function will return a frame index where a swap in and swap out will occur
            f=findFrameForOptimal(n,i,frameList)
            print(str(frameList[f])+" is replaced with "+str(refString[i]))
            frameList[f]=refString[i]
            pageFaultCnt+=1
    
    print('total page fault:  ')
    print(pageFaultCnt)
    rate=(pageFaultCnt/len(refString))*100
    print(str(rate)+'%')


#driver code
#print('Using FIFO: ')
#fifo(3)
print('Using Optimal page replacement: ')
OptimalPageRepalce(3)