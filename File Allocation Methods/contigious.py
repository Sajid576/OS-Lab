print("Enter the number of blocks:  ")
total_blocks=200
print(total_blocks)


#this list used to store the info of a file.
#file contains info like-
#(starting block,file size,file name)
FilesInfo=[
   (20,40,'D'),
   (130,70,'E')
]
FilesInfo.sort()


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
    for i in range(len(FilesInfo)):
        starting=FilesInfo[i][0]
        if((starting-myFileSize)> FilesInfo[i-1][0]+FilesInfo[i-1][1] ):
            writeFile(starting,myFileSize,myFileObj)
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


#driver code

insertFile('A',4)
insertFile('B',400)
insertFile('C',40)

print(FilesInfo)







