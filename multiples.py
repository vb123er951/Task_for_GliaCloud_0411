M = []
N = 1000

### initialize
for i in range(N):
	M.append(0)

### find multiples of 3 and 5
for i in range(1, N):
	if M[i] == 1:
		continue
	if (i % 3 == 0 or i % 5 == 0) and M[i] == 0:
		M[i] = 1
		for j in range(2, N):
			if i * j < N:
				M[i*j] = 1
			else:
				break

sum = 0				
for i in range(N):
	if M[i] == 1:
		sum += i
	#print (i, M[i])
print (sum)