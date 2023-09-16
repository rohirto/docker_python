""" Control Flow examples """
# Sequences
print("This ")
print("is  a ")
print("Sequence")

#Iterations
# For used when you know the no of iteratons to be executed

for i in range(3):
    print(f"This is iteration{i}")


# Selections
if 7 in range(3):
    print("This is not going to be printed")
elif 1 in range(3):
    print("This will be printed")
else:
    print("Else last")

#while loop
# While used when no of iterations not known
j = 0
while j < 3:
    print(f"This is iteration {j}")
    j = j + 1
