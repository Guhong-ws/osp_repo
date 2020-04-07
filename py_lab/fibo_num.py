num = int(input("fibonacci number? "))

fibo = [1,1]
val = []

for i in range(2, num):
	val = fibo[-1] + fibo[-2]
	fibo.append(val)

print(fibo)
print('F%d = %d' %(num ,fibo[-1]))

