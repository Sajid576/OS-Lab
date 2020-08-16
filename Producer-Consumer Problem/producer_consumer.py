import threading
import time

'''
counter=0
Producer thread increases the counter .
Consumer thread decreases the counter. 
if counter is less than 1 ,then Consumer thread goes to sleep and doesn't wake up until the counter is greater
or equal than 1 .

else if counter is equal to the size of buffer , then producer goes to sleep and doesnt wake up until 
the counter is less than buffer size-1 .


'''
threadLock = threading.Lock()
threads=[]
buff_size=10
buff=[0]*buff_size
counter=0


class myThread (threading.Thread):
    def __init__(self, threadID, name, data):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.data = data
    
   
    def run(self):
        # Get lock to synchronize threads
        threadLock.acquire()
        print ("Starting " + self.name)
        updateCounter(self)
        print ("Exiting " + self.name)
        # Free lock to release next thread
        threadLock.release()

def updateCounter(self):
    global counter
    time.sleep(2)
    if(self.name=='producer' and counter < buff_size-1 ):
        buff[counter]=int(self.data)
        counter+=1
        print(self.data+" is inserted in the buffer")

    elif( self.name=='consumer' and counter>0):
        data=int(buff[counter])
        counter-=1
        print(str(data)+" is consumed from the buffer")
        




# driver code
print("Enter the number of threads: ")
num_of_threads=int( input())

for i in range(0,num_of_threads):
    threadName=str(input('Select p for producer OR c for consumer: '))
    threadId=int(input('Enter id of '+threadName+': '))
    if(threadName=='p'):
        data=input('Enter the data to insert in the buffer:  ')
        thread = myThread(threadId,threadName, data)
    else:
        #consumer thread will initially have 0 in the data field
        thread = myThread(threadId,threadName,0)

    threads.append(thread)

print("*******Threads are starting**********")
# Start new Threads in threads list
for thread in threads:
    thread.start()




