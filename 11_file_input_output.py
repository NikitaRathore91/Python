#python can be used to perform operations on a file (read and erite data)
# types of all files
# 1. Text files: txt,bdocx, .log, etc
# 2. Binary Files : mp4, .mov, .png, .jpeg, etc
 
# ----------open, read , close
#syntax:  f = open("file_name","mode")   mode:- read mode, write mode 
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()
 