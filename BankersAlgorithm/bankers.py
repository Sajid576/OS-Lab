#it is a brute force approach 
  
# Function to find the need of each process  
def calculateNeed(need, maxm, allot): 
    for i in range(P): 
        for j in range(R):         
            # Need  = maxm  -  allocated 
            need[i][j] = maxm[i][j] - allot[i][j]  
  

def isSafe( avail, maxm, allot): 
    need = [] 
    for i in range(P): 
        l = [] 
        for j in range(R): 
            l.append(0) 
        need.append(l) 
   
    # Function to calculate need matrix  
    calculateNeed(need, maxm, allot) 
  
    # Mark all processes as in finish  
    finish = [0] * (P+1) 
      
    # To store safe sequence  
    safeSeq = [0] * P  
  
    # Make a copy of available resources  
    work = [0] * R  
    for i in range(R): 
        work[i] = avail[i]  
  
    print('avalable array: ')
    print(work)
    # While all processes are not finished  
    # or system is not in safe state.  
    count = 0
    while (count < P): 
          
        # Find a process which is not finish  
        # and whose needs can be satisfied  
        # with current work[] resources.  
        found = False
        for p in range(P):  
          
            # First check if a process is finished,  
            # if no, go for next condition  
            if (finish[processes[p]] == 0):  
              
                # Check if for all resources  
                # of current P need is less  
                # than work 
                for j in range(R): 
                    if (need[p][j] > work[j]): 
                        break
                      
                # If all needs of p were satisfied.  
                if (j == R - 1):  
                  
                    # Add the allocated resources of  
                    # current P to the available/work  
                    # resources i.e.free the resources  
                    for k in range(R):  
                        work[k] += allot[p][k]
                      
                    print(work)
                    # Add this process to safe sequence.  
                    safeSeq[count] = processes[p]
                    count += 1
  
                    # Mark this p as finished  
                    finish[processes[p]] = 1
  
                    found = True
                  
        # If we could not find a next process  
        # in safe sequence.  
        if (found == False): 
            print("System is not in safe state") 
            return False
          
    # If system is in safe state then  
    # safe sequence will be as below  
    print("System is in safe state.", 
              "\nSafe sequence is: ", end = " ") 
    print(safeSeq)  
    print("Need list")
    print(need)
    return True



P = 5
R = 3

# Resources allocated to processes  
allot = [
            [0, 1, 0], 
            [2, 0, 0], 
            [3, 0, 2], 
            [2, 1, 1], 
            [0, 0, 2]
        ]  
# Maximum R that can be allocated   to processes  
maxm = [
            [7, 5, 3],
            [3, 2, 2], 
            [9, 0, 2], 
            [2, 2, 2], 
            [4, 3, 3]
        ] 
  

# total instances of resources
total=[10,5,7]

# Available instances of resources  
avail = [] 

#seq--> 2,4,5,1,3



# Driver code  
#P=int(input('Number of processes:  '))
#R=int(input('Number of resources:  '))
processes = [1, 2, 3, 4,5] 



'''
for i in range(P):
    
    print("Process:  "+str(processes[i]))
    temp=[]
    for j in range(R):
        
        val =int(input("Maximum value for resource "+str(j+1)+": "))
        temp.append(val)
    maxm.append(temp)
   
    temp=[]
    for j in range(R):
        
        val =int(input("allocation from resource "+str(j+1)+": "))
        temp.append(val)
    allot.append(temp)
  


total_numberOfResources=[]
print('Enter the total instances of resources')
total_numberOfResources=input().split()
for i in range(R):
    c=int(total_numberOfResources[i])
    total_numberOfResources[i]=c


'''



total_allocated=[0]*R
for i in range(R):
    sum=0
    for j in range(P):
        sum += allot[j][i]

    total_allocated[i]=sum

avail=[0]*R
for i in range(R):
    avail[i]= total[i]-total_allocated[i]


# Check system is in safe state or not  
isSafe (avail, maxm, allot)  
