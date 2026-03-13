import array as arr

array_num=arr.array("i", [1,2,3,3,4,5,3,2,4,3,3])
print("Original array:",str(array_num),"\n")

print("Number of occurences of the number three 3 in the given array:", str(array_num.count(3)), "\n")


array_num.reverse()
print("Reverse of the Original array's order of elements:", str(array_num))