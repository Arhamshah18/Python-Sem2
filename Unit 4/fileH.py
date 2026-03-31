#File Handling in Python 

#Opening file in write mode to write data
file = open("file.txt","w")
file.write("First Line of File")
file.write("\n2nd line !!!!!!! ")
file.close()#Closing of file 

print("Data written Sucessfully") 
 
#Opening file in read mode to read contents
file = open("file.txt","r")
print(file.read()) 
file.close()
