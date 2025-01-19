file=open("abc.txt","r")
counter=0
content=file.read()
colist=content.split("\n")
for i in colist: 
    if i:
        counter+=1 
        print(counter)