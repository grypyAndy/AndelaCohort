#function to list all the prime numbers from 0 to n
def primeNum_list(n):
	
	for i in range (2,n):
		primes=True
		for h in range (2,i):
			if (i%h==0):
				primes=False
				break
		if primes:
			print(i)






primeNum_list(25)


