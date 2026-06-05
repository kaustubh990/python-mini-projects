#file i/o
#read file
f=open("E:\college related\WEB D\python\practice.py","r")

data = f.read()
#data = f.read(7)
print(data)

line1 = f.readline()
print(line1)
f.close

#write file
f=open("E:\college related\WEB D\python\practice.py","a")

data = f.write()


"""modes are r,w,a
r+=read,overwrite(pointer starting me), no truncate means no deletion of data
w+=read and write ,truncate
a+=read and append,pointer end,notruncate
"""
