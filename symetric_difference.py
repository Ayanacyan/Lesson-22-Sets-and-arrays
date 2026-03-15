seta1={'blue','green'}
seta2={"blue", 'yellow'}

print("First set of elements")
print(seta1,"\n")
print(seta2,"\n")

print("Symetric differnce of first pair of sets")
seta3=seta1.symmetric_difference(seta2)
print(seta3)

setb1={1,2,3,4,5}
setb2={1,5,6,7,8,9}

print("\nSecond set of elements")
print(setb1,"\n")
print(setb2,"\n")

print("Symetric differnce of the second pair of sets")
setb3=setb1.symmetric_difference(setb2)
print(setb3)