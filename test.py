import sys

data = sys.stdin.read()
file = open("testfile.txt","a") 

if data == "open\n":
   file.write("\nstart recording\n")

else: 
   file.write("stop recording\n")

file.close
