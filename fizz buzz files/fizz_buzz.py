def fizz_buzz(num):
	a='Fizz'
	b='Buzz'
	c='FizzBuzz'
	if num%3==0 and num%5==0:
		return c
	elif num%3!=0 and num%5!=0:
		return num
	elif num%5==0:
		return b
	elif num%3==0:
		return a
	
