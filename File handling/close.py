#9
#using with open statement the file automically closes where as using 
#direct open it should be closed .

#Eg:using direct open
# f=open('data.txt','r')
# print(f.closed)
# f.close()
# print(f.closed)

#eg:using with open
# with open("data.txt","r") as f:
#     pass
# print(f.closed) #prints True