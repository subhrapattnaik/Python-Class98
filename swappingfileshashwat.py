#create a new file
#f=open("sample11.txt","x")
#f=open("sample12.txt","x")


with open("sample11.txt", 'r') as a:
    data_a = a.read()
     

with open("sample12.txt", 'r') as b:
    data_b = b.read()
    

with open("sample11.txt", 'w') as a:
    a.write(data_b)
    

with open("sample12.txt", 'w') as b:
    b.write(data_a)