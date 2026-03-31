#File Handling Operations
filename = "file2"

#Writing to a file (creates a new file or overwrites) 
with open(filename, "w") as file:
    file.write("This is the first line of the file.\n")
    print(f"Successfully wrote to {filename}")

#Reading file 
print("Contents in file : \n")
file=open(filename,'r') 
print(file.read())
file.close()

#Appending to a file
with open(filename, "a") as file:
    file.write("This is an appended line.\n")
    print(f"Successfully appended to {filename}")

#Reading file 
print("***Reading again***")
print("Contents in file : \n")
file=open(filename,'r') 
print(file.read())
file.close()

#Using 'with' automatically handles closing the file 