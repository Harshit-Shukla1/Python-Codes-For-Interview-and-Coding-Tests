arr=[1,2,3,4,5];
n=3
for i in range(0,n):
    last = arr[len(arr)-1];
    for j in range(len(arr)-1,-1,-1):
        arr[j]=arr[j-1];
    arr[0]=last;
print();
print("left rotation");
for i in range(0,len(arr)):
    print(arr[i],end=" ");