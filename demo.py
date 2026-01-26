
f=open("file.txt","r")#r
content=f.read(10)#fun inside give 10 the give first ten vlue
print(content)
#print(f.readline())#line by line read
f.close()
name = input()
mark =int (input())
Department=input()
print("my name is:",name)
print("MY mark is:",mark/10,"/10")
print("my department is:",Department)
