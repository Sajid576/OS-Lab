print("Enter the number of blocks:  ")
total_blocks=200
print(total_blocks)


#this list used to store the info of a file.
#file contains info like-
#(starting block,file size,file name)
FilesInfo=[
   (0,40,'D'),
   (130,70,'E')
]
FilesInfo.sort()
print('Disk state: ')
print(FilesInfo)

#this method used to find the empty blocks on hdd.If there is
#enough empty blocks then the inserted file is ready to be written 
#on hdd.
def findEmptyBlock(myFileObj):
    myFileSize=myFileObj['blocksize']

    #find free space from first portion
    if((FilesInfo[0][0]-myFileSize)>0):
        starting=FilesInfo[0][0]
        writeFile(starting,myFileSize,myFileObj)
        return
    #find free space from last portion
    if(FilesInfo[len(FilesInfo)-1][0] + FilesInfo[len(FilesInfo)-1][1] + myFileSize < total_blocks ):
        starting=FilesInfo[len(FilesInfo)-1][0] + FilesInfo[len(FilesInfo)-1][1]
        writeFile(starting,myFileSize,myFileObj)
        return

    #find free space from middle portion
    for i in range(1,len(FilesInfo)):
        starting=FilesInfo[i][0]
        #print('lel')
        #print(i)
        #print(FilesInfo[i-1][0])
        if( (starting-myFileSize)  > FilesInfo[i-1][0] + FilesInfo[i-1][1] ):
            writeFile(starting,myFileSize,myFileObj)
            print('middle')
            return

    print("Not enough space")   
    return

#this method will be called after checking 
def writeFile(starting,myFileSize,myFileObj):
    newStarting=starting-myFileSize
    newFileName=myFileObj['filename']
    FilesInfo.append((newStarting,myFileSize,newFileName))
    FilesInfo.sort()

    print("File "+newFileName+" created")


def insertFile(fileName,blockSize):
    myFileObj={}
    myFileObj['filename']=fileName
    myFileObj['blocksize']=blockSize
    
    findEmptyBlock(myFileObj)


def searchFile(fileName):
    
    for file in  FilesInfo:
        if(fileName==file[2]):
            print(fileName+' file found in:')
            for i in range(file[0],file[0]+file[1]+1):
                print(str(i),end=', ')

            print('\n')
            return
    print(fileName+' File not found')
    return 

#driver code

insertFile('A',4)
insertFile('B',400)
insertFile('C',40)
'''
searchFile('A')
searchFile('Z')
searchFile('B')
searchFile('C')
searchFile('D')
'''
print('Disk state: ')
print(FilesInfo)







