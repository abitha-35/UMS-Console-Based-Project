#method 1
'''x=open("hello.txt","r")
x.close'''

#method 2
'''x=open("hello.txt","r")
data=x.read()
print(data)
x.close()'''

#method 3
'''x=open("hello.txt","r")
data=x.readlines()
print(data)
x.close()'''

#method 4
'''x=open("hello.txt","r")
data=x.read()
for i in data:
    print(i)
x.close()'''

#method 5
'''x=open("hello.txt","r")
data=x.read(10)
print(data)
x.close()'''

#write mode

#method 1
'''x=open("hello3.txt","w")
x.write("hello abitha")
x.close()'''

#append mode

#method 1
x=open("hello3.txt","a")
x.write("data 1")
x.close()




