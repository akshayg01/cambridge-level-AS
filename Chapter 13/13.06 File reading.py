file_object = open('D:\\workspace\\cambridge-level-AS\\Chapter 13\\test2.txt', 'r')
#print(file_object.readline())
#print(file_object.readlines())
print(file_object.tell())

count = 0
while(count<8):
    print(file_object.readline())
    print(file_object.tell())
    count= count + 1
file_object.close()