num = int(input("Number of input : "))

total = 0

for i in range (0, num):
	value = int(input())
	total = total + value

average = total/num

print('Average: ', average)
