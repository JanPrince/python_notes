"""
problem : finding the cube root of a number
"""
cube = 8
for guess in range(cube + 1):
    if guess ** 3 == 8:
        print("the cube root of ",cube, 'is', guess)
        break    # this breaks out of the loop exactly when we have our answer. This reduces runtime

print('\n')

# modified code to handle -ve cubes and non-perfect cubes
cube_num = int(input("enter cube: "))
for guesss in range(abs(cube_num)+1):
    if guesss**3 >= abs(cube_num):
        break
if guesss **3 != abs(cube_num):
    print("number ain't a perfect cube")
elif guesss**3 == cube_num:
    print("hurray, ans is ", guesss)
else:
    if cube_num < 0:
        guesss = -guesss
        print("cuberoot of ", cube_num, "is", guesss)
