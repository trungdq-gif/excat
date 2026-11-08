arr = [1,2,3,4,5,6,7,8]
b = [2]
for _ in range(3):
	b.append(arr.pop(0))
print(b)