import threading
import time

threadLock = threading.Condition()
threads=[]



class MyThread (threading.Thread):
    def __init__(self, threadID, name, data):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.data = data
    
   
    def run(self):
        middleWere(self)
       

def middleWere(self):
    
    # Get lock to synchronize threads
    threadLock.acquire()
    
    print('\n')
    print ("Starting " + self.name+"-"+str(self.threadID))
    updateCounter(self)
    print ("Exiting " + self.name+"-"+str(self.threadID))
    # Free lock to release next thread
    try:
        threadLock.notify()
        threadLock.release()
    except (RuntimeError, TypeError, NameError):
        pass

def updateCounter(self):
    global full,empty
    time.sleep(2)
    if(self.name=='p' ):
        come_back_again=0
        if(full < buff_size):

            if(len(self.data)>0):
                d=self.data.pop(0)
                if(len(self.data)>0):
                    come_back_again=1
                        
            buff[full]=int(d)
            full+=1
            empty-=1
            print(str(d)+" is inserted in the buffer")
            print('State of buffer is:  '+str(buff))
            print('Number of filled up spaces: '+str(full))
            print('Remaining empty spaces: '+str(empty))
        else:
            if(len(self.data)>0):
                come_back_again=1
            print('buffer is full.Come back later, producer')


        
        if(come_back_again==1):
            print(self.name+'-'+str(self.threadID)+" will come back again")
            try:
                threadLock.notify()
                threadLock.release()
                middleWere(self)
            except (RuntimeError, TypeError, NameError):
                middleWere(self)
                
    elif( self.name=='c' ):
        if(full>0):
            full-=1
            data=int(buff[full])
            buff[full]=0
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
    print('\n')
    threadName=str(input('Select p for producer OR c for consumer: '))
    threadId=int(input('Enter id of '+threadName+': '))
    if(threadName=='p'):
        dataSize=int(input('Enter the number of data of '+threadName+'-'+str(threadId) +':  '))
        data=[]
        for i in range(dataSize):
            d=int(input())
            data.append(d)

        thread = MyThread(threadId,threadName, data)
    else:
        #consumer thread will initially have 0 in the data field
        thread = MyThread(threadId,threadName,0)

    threads.append(thread)

print("*******Threads are starting**********")
# Start new Threads in threads list
for thread in threads:
    thread.start()




