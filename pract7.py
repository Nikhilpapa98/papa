#pract 7
import array as a
arr = a.array( 'i',[20,40,60,80,100])
print(arr)
arr.insert(2,50)
print(arr)
print("first element",arr[0])
print("last element",arr[-1])
print("second element",arr[1])
print("third to fifth ",arr[2:5])
print("from beginning to 3rd ",arr[:3])
print("fourth to end ",arr[3:])
print("start to end ",arr[:])
