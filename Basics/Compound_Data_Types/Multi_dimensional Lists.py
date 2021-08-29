# A good way to visualize a 2d array is a list of lists

lst = [[1,2,3], [4,5,6], [7,8,9]]

print(lst[1][2])
lst[1] = [45,12,3]

print(lst[1][2])

lst.append([67,8,-1])
print("length of lst = ", len(lst))
