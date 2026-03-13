my_set={1,2,3,4}
print(my_set)

my_set={1.0,"hello", (1,2,3,4)}
print(my_set)

my_set={1,2,3,4,5,4,3,2,1}
print(my_set)

my_set=set([1,2,3,4,3])
print(my_set,"\n")

num_set=set([0,1,2,3,4])
print("Original Set", num_set)
num_set.pop()
print("After removing the first element", num_set,"\n")