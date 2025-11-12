#Read Write and Append

'''
Step 1 : Connect to a file 
Step 2 : Read, Write or append
Step 3 : Disconnect from the file
'''

#Append 

Variable = open(file='file_name', mode="a")
variable.close

#Write

Variable = open(file='file_name', mode="w")
Variable.write(Str(X))
Variable.write(y)

#Multiple Write 

L = [Str(X)+"\n", y+"\n"]
Variable.writelines(L)

# Printing things in File 

print(X,Y,20,"Hey",sep="\n", file="File_name")

# Reading 

Variable = open(file='file_name', mode="r")
file_content = Variable.read()
print(file_content \n)

# Reading Multiple Lines

for file_content in Variable:
  file_content = Variable.readline()
  print(file_content)

or 

file_content = my_out_file_handle.readline()

or 

while True:
  file_content = my_out_file_handle.readline()
  if file_content=="":
    break 
  else:
    print("file_content:", file_content)

#Notes
'''
We have functions for all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read or write
    - FOR WRITING: 1) write() method 2) writelines() method 3) print-function
    - FOR READING: 1) read() method 2) readlines() method 3) readline() method
Step-3: Disconnect from file
    - close() method
'''
# -----------
# Modes:
'''
# mode "w":
#       - It is, write only mode
#       - It will create new file
#       - IMPORTANT: it will erase existing file-content
#
# mode "r":
#       - It is, read only mode
#       - It will NOT create new file
#
# mode "a":
#       - It is, append/write only mode
#       - It will create new file only if file not present
# NOTE:
#   - if we add + to each mode then it will enable read/write mode
#       Example: 'w+', 'r+', 'a+'
#   - if we add 'b' to each mode then it will be binary file
#       Example: 'wb', 'rb', 'ab'
'''


