# here,elements of refString denotes the page number of the process 
#refString=[4,5,6,9,6,7,9]

refString=[7,5,3,4]


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

    print(pageFaultCnt)
    rate=(pageFaultCnt/len(refString))*100
    print(rate)
    print('%')


def findFrameForOptimal(n,refIndx,frameList):
    
    #this list used for keeping track of the target frame
    #  index where replacement will occur
    targetFrameList=[]

    #this var used for setting a frame index highest priority
    # for the replacement.This will occur when a value of
    #a particular frame wont be found after refIndx.

    MAX_PRIOR=1000000
    #print(str(frameList)+"--->"+str(refIndx))
    for i in range(len(frameList)):
        
        try:
            #value is searched after refIndx
            indx=refString.index(frameList[i],refIndx)
            targetFrameList.append((indx,i))
        except ValueError:
            indx=MAX_PRIOR
            targetFrameList.append((indx,i))

   
    
    targetFrameList.sort(key=lambda x: x[0],reverse=True)
    if(targetFrameList[0]==MAX_PRIOR):
        print("fifo will be applied")
    #print(targetFrameList[0][1])
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
            frameList[f]=refString[i]
            pageFaultCnt+=1

        print("RAM: "+str(frameList))
        print(pageFaultCnt)

    print("total page fault: ")
    print(pageFaultCnt)
    rate=(pageFaultCnt/len(refString))*100
    print(rate)
    print('%')



def findFrameForLRU(n,refIndx,frameList):
    
    #this list used for keeping track of the target frame
    #  index where replacement will occur
    targetFrameList=[]

    #this var used for setting a frame index highest priority
    # for the replacement.This will occur when a value of
    #a particular frame wont be found before refIndx.

    MAX_PRIOR=-1000000
    #print(str(frameList))
    for i in range(len(frameList)):
        
        indx=MAX_PRIOR
        #finding last occurences of elements
        for j in range(0,refIndx):
            if(refString[j]==frameList[i]):
                indx=j
        targetFrameList.append((indx,i))
           
            

    targetFrameList.sort(key=lambda x: x[0])
    if(targetFrameList[0]==MAX_PRIOR):
        print("fifo will be applied")
    #print(targetFrameList)
    #print(targetFrameList[0][1])
    return targetFrameList[0][1]

def LRU(n):
    #size of RAM/total number of frames
    
    frameList=[-1]*n
    pageFaultCnt=0

    
    #f denotes the frame index
    f=0
    for i in range(0,len(refString)):
        
        if(refString[i] not in frameList):
            #this function will return a frame index where a swap in and swap out will occur
            f=findFrameForLRU(n,i,frameList)
            
            frameList[f]=refString[i]
            pageFaultCnt+=1

        print("RAM: "+str(frameList))
        print(pageFaultCnt)
        print('\n')

    print("total page fault: ")
    print(pageFaultCnt)
     



def LRUusingStack(n):
    #n=size of RAM/total number of frames
    
    frameList=[-1]*n
    pageFaultCnt=0

    
    for i in range(0,len(refString)):
        
        if(refString[i] not in frameList):
            frameList.pop(0)
            
            frameList.append(refString[i])
            pageFaultCnt+=1
        else:
            f=frameList.index(refString[i])
            frameList.pop(f)
            
            frameList.append(refString[i])

        print("RAM: "+str(frameList))
        print(pageFaultCnt)
        print('\n')

    print("total page fault: ")
    print(pageFaultCnt)


def secondChance(n):
    #n=size of RAM/total number of frames
    
    frameList=[(-1,0)]*n    #(data,reference bit)
    pageFaultCnt=0
    
    for i in range(0,len(refString)):
        
        if(refString[i] not in frameList):

            pageFaultCnt+=1     #page fault ++

            r_bit = frameList[0][1]
            if(r_bit==0):
                frameList.pop(0)
                frameList.append( (refString[i],1) )
            else:
                #if r_bit==1 , the first element gets a 2nd chance .So,it gets popped from first 
                #place and gets appened to the last
                while(frameList[0][1]==1):
                    p=frameList.pop(0)
                    frameList.append( ( p[0],0 ) )
                frameList.pop(0)
                frameList.append( (refString[i],1) )
        else:
            for i in range(0, len(frameList) ):
                if(frameList[i][0]==refString[i]):
                    print('2nd chance got')
                    frameList[i][1]=1

        print('RAM:  '+str(frameList))
        print('page fault: '+str(pageFaultCnt))
        print('\n\n')                



#driver code
#print("using fifo:  ")
#fifo(3)
#print("using OPR:  ")
#OptimalPageRepalce(3)
#print("using LRU:  ")
#LRU(8)
#print('LRU using stack: ')
#LRUusingStack(3)

#print("Second chance algorithm:  ")
#secondChance(3)
