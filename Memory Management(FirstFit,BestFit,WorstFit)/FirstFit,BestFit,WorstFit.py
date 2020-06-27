

processSize=[100,10,35,15,23,6,25,55,88,40]

memoryHoleSize=[50,200,70,115,15]




def firstFit():
    allocation=[-1]*len(processSize)

    holes=[]
    for i in range(len(memoryHoleSize)):
        holes.append(memoryHoleSize[i])

    for i in range(len(processSize)):
        flag=0
        for j in range(len(holes)):
            
            if(processSize[i]<=holes[j]):
                allocation[i]=j
                holes[j]-=processSize[i]
                flag=1
                break
        if(flag==0):
            val="External Fragmentation"
            print(val)
            return allocation
    
    val="No external fragmentation"
    print(val)
    return allocation


def bestFit():
    allocation=[-1]*len(processSize)

    holes=[]
    for i in range(len(memoryHoleSize)):
        holes.append(memoryHoleSize[i])

    for i in range(len(processSize)):
        bestIndx=-1
        for j in range(len(holes)):
            if(processSize[i]<=holes[j]):
                if(bestIndx==-1):
                    bestIndx=j
                elif(holes[bestIndx]>holes[j]):
                    bestIndx=j    
        if(bestIndx!=-1):
            allocation[i]=bestIndx
            holes[bestIndx]-=processSize[i]
        else:
            print("External fragmentation")
            return allocation
    
    print("No external allocation")
    return allocation

def worstFit():
    allocation=[-1]*len(processSize)

    holes=[]
    for i in range(len(memoryHoleSize)):
        holes.append(memoryHoleSize[i])

    for i in range(len(processSize)):
        wstIndx=-1
        for j in range(len(holes)):
            if(processSize[i]<=holes[j]):
                if(wstIndx==-1):
                    wstIndx=j
                elif(holes[wstIndx]<holes[j]):
                    wstIndx=j    
        if(wstIndx!=-1):
            allocation[i]=wstIndx
            holes[wstIndx]-=processSize[i]
        else:
            print("External fragmentation")
            return allocation
    
    print("No external allocation")
    return allocation

alloc=firstFit()
print(alloc)
alloc=bestFit()
print(alloc)
alloc=worstFit()
print(alloc)