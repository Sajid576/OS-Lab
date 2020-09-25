import json
total_blocks=200


#this dictionary key(index block) stores the list of all blocks of a file
FilesInfo={
    6:([9,1,14,4],'E'),
    2:([3,5,7,10,11],'D')
}
filledupBlocks=[2,1,3,4,5,6,7,9,10,11,14]
blankBlocks=[0,8,12,13,15,16,17,18,19]

print("total blocks: "+str(total_blocks))
print("disk state:  ")
print(json.dumps(FilesInfo, indent=4))
print('filled up blocks: ')
print(filledupBlocks)
print('blank blocks: ')
print(blankBlocks)
print('\n\n')
def findEmptyBlock(myFileObj):
    myFileSize=myFileObj['blocksize']
 
    #a file will fillup number of blocks which is equal to 
    #the fileSize and extra 1 block will be filled up for 
    #index block of that file
    if(len(blankBlocks) >= myFileSize+1):
            writeFile(myFileSize,myFileObj)
            return
    else:
        print("Not enough space")
        return

def writeFile(myFileSize,myFileObj):
    myFileName=myFileObj['filename']

    #1st pop for filling index block 
    u=blankBlocks.pop(0)
    filledupBlocks.append(u)

    temp_list=[]
    for i in range(myFileSize):
        v=blankBlocks.pop(0)
        filledupBlocks.append(v)
        temp_list.append(v)

    FilesInfo[u]=(temp_list,myFileName)
    print("File "+myFileName+" created")

def insertFile(fileName,blockSize):
    myFileObj={}
    myFileObj['filename']=fileName
    myFileObj['blocksize']=blockSize
    
    findEmptyBlock(myFileObj)


def searchFile(fileName):
    for keys,values in FilesInfo.items():
        if(fileName== values[1]):
            print(fileName+' found in ')
            print(str(keys) +','+str(values[0]))
            print('\n')
            return 

    print(fileName+' file not found ')
    return 

#driver code

insertFile('A',4)
insertFile('B',2)
insertFile('C',8)

searchFile('A')
searchFile('D')
searchFile('C')


print("disk state:  ")
print(json.dumps(FilesInfo, indent=4))
print('filled up blocks: ')
print(filledupBlocks)
print('blank blocks: ')
print(blankBlocks)
print('\n\n')