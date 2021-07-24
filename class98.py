
#open file
f=open("sample1.txt")

#same as below
#f=open("sample1.txt","rt")

#open() returns a file object, which has a read() method for reading the contents of the file
#print(f.read())

#if file is located ina different location ,give the file path


#by default read() returns the whole text.but you can specify how many characters you want to returns
#print(f.read(5))


#you can return one line by using readline() method
#print(f.readline())

#by calling readline() two times,you can read the first two lines
#print(f.readline())
#print(f.readline())



#by looping through the lines of the file ,you can read the whole file,line by line
#f=open("sample1.txt","r")
#for x in f:
  #print(x)


#close files
#it is a good practice to always close file when you are done
#f=open("sample1.txt","r")
#print(f.readline())
#f.close()

#write to an existing file
#add a parameter to the open() function
#"a"- append-will append to the end of the file
#"w"-write-will overwrite any existing content

#f=open("sample2.txt","a")
#f.write("hellllllllllllllllllllllllllllo")
#f.close()

#open and read the file after appending
#f=open("sample2.txt","r")
#print(f.read())


#"w"--is for over writting the content
#f=open("sample2.txt","w")
#f.write("OOps!!I have deleted the content")
#f.close()

#open and read the file after the overwritting
#f=open("sample2.txt","r")
#print(f.read())

#create a new file(a new empty file will be created)
#f=open("myfile.txt","x")

#create a file if doesnot exists
#f=open("myfile2.txt","w")

#delete a file
import os
#os.remove("myfile.txt")

#check if file exists or not
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exists")

#delete folder
import os
os.rmdir("myfolder")












