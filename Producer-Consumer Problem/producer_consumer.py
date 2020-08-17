import threading
import time

'''
To learn more about python threads visit here: https://www.tutorialspoint.com/python/python_multithreading.htm#:~:text=The%20threading%20module%20provided%20with,force%20threads%20to%20run%20synchronously.


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



class myThread (threading.Thread):
    def __init__(self, threadID, name, data):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.data = data
    
   
    def run(self):

        # Get lock to synchronize threads
        threadLock.acquire()
        print('\n\n')
        print ("Starting " + self.name+"-"+str(self.threadID))
        updateCounter(self)
        print ("Exiting " + self.name+"-"+str(self.threadID))
        # Free lock to release next thread
        threadLock.release()

def updateCounter(self):
    
    global full,empty
    time.sleep(2)
    if(self.name=='p' ):
        if(full < buff_size):

            buff[full]=int(self.data)
            full+=1
            empty-=1
            print(self.data+" is inserted in the buffer")
            print('State of buffer is:  '+str(buff))
            print('Number of filled up spaces: '+str(full))
            print('Remaining empty spaces: '+str(empty))
        else:
            print('buffer is full.Come back later, producer')

    elif( self.name=='c' ):
        if(full>0):
            full-=1
            data=int(buff[full])
            
            empty+=1
            print(str(data)+" is consumed from the buffer")
            print('State of buffer is:  '+str(buff))
            print('Number of filled up spaces: '+str(full))
            print('Remaining empty spaces: '+str(empty))
        else:
            print('no item in the buffer.Come back later,Consumer')




# driver code
buff_size=int( input("Enter the size of buffer: "))
num_of_threads=int( input("Enter the number of threads: "))

buff=[0]*buff_size
empty=buff_size
full=0
for i in range(0,num_of_threads):
    print('\n\n')
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




