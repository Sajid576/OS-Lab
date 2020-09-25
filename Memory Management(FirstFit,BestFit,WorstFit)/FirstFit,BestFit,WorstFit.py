
#10
requests=[100,10,35,15,88]
#5
memoryHoleSize=[50,200,70]
#requests=[]
#memoryHoleSize=[]

def firstFit():
    #allocation=[-1]*len(requests)

    holes=[]
    for i in range(len(memoryHoleSize)):
        holes.append(memoryHoleSize[i])

    for i in range(len(requests)):
        flag=0
        for j in range(len(holes)):
            
            if(requests[i]<=holes[j]):
                #allocation[i]=j
                holes[j]-=requests[i]
                flag=1
                break
        if(flag==0):
            print(requests[i])
            print(holes)
            total_sum=sum(holes)
            print("External Fragmentation  "+str(total_sum))
            return 
            #return allocation
        else:
            print(requests[i])
            print(holes)


    
    print("No external fragmentation")
    


def bestFit():
    #allocation=[-1]*len(requests)

    holes=[]
    for i in range(len(memoryHoleSize)):
        holes.append(memoryHoleSize[i])

    for i in range(len(requests)):
        bestIndx=-1
        for j in range(len(holes)):
            if(requests[i]<=holes[j]):
                if(bestIndx==-1):
                    bestIndx=j
                elif(holes[bestIndx]>holes[j]):
                    bestIndx=j    
        if(bestIndx!=-1):
            #allocation[i]=bestIndx
            holes[bestIndx]-=requests[i]
            print(requests[i])
            print(holes)
        else:
            print(requests[i])
            print(holes)
            total_sum=sum(holes)
            print("External fragmentation"+str(total_sum))
            return
            #return allocation
    
    print("No external fragmentation")
    #return allocation

def worstFit():
    #allocation=[-1]*len(requests)

    holes=[]
    for i in range(len(memoryHoleSize)):
        holes.append(memoryHoleSize[i])

    for i in range(len(requests)):
        wstIndx=-1
        for j in range(len(holes)):
            if(requests[i]<=holes[j]):
                if(wstIndx==-1):
                    wstIndx=j
                elif(holes[wstIndx]<holes[j]):
                    wstIndx=j    
        if(wstIndx!=-1):
            #allocation[i]=wstIndx
            holes[wstIndx]-=requests[i]
            print(requests[i])
            print(holes)
        else:
            print(requests[i])
            print(holes)
            total_sum=sum(holes)
            print("External Fragmentation  "+str(total_sum))
            return
            #return allocation
    
    print("No external allocation")
    #return allocation


#driver code

#n=int(input('Enter number of request: '))
#m=int(input('Enter number of processhole: '))
#print('Enter request list:  ')
#for i in range(n):
 #   val=int(input())
 #   requests.append(val)

#print('Enter process list:  ')
#for i in range(m):
 #   val=int(input())
  #  memoryHoleSize.append(val)

print('first fit:  ')
firstFit()
print('\n\n')
print('best fit:  ')
bestFit()
print('\n\n')
print('worst fit:  ')
worstFit()
