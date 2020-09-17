# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 
	multiplication = num1 * num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic 
	if(num2==0):	#Guard Code to prevent division by zero
		return 0
	division = num1 / num2
	return division

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	#Power Logic
	#check_1 = isinstance(num1,(int))
	check_2 = isinstance(num2,(int))
	if(check_2== False and num2-int(num2)!=0):
		return 0

	power = 0	#By default we have to return 0 in case of any error

	num1=int (num1)
	num2= int(num2)

	if(num1>0):
		dummy_power=1
		if(num2>0):
			#dummy_power=1
			for i in range(num2):
				dummy_power*=num1
		
		elif(num2==0 ):
			dummy_power = 1
		elif(num2<0):
			for i in range(-num2):
				dummy_power*=num1
			dummy_power = 1/dummy_power



	elif(num1==0):
		dummy_power=0
	
	elif(num1<0):
		
		dummy_power=1
		if(num2>0):
			#dummy_power=1
			for i in range(num2):
				dummy_power*=-num1
		
		elif(num2==0):
			dummy_power = 1
		elif(num2<0):
			for i in range(-num2):
				dummy_power*=-num1
			dummy_power = 1/dummy_power
		if(abs(num2)%2!=0):
			dummy_power*=-1



	power= dummy_power	
	return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	check_n = isinstance(n,int)
	if(check_n==False and n-int(n)!=0):
		return [0]
	gp=[]
	term_i= a
	gp.append(a)

	for i in range(int(n-1)):
		term_i*= r
		gp.append(term_i)

	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	check_n = isinstance(n,int)
	if(check_n==False and n-int(n)!=0):
		return [0]
	ap=[]
	term_i=a
	ap.append(a)
	for i in range(int(n-1)):

		term_i+=d
		ap.append(term_i)

	
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	check_n = isinstance(n,int)
	if(check_n==False and n-int(n)!=0):
		return [0]
	hp=[]

	reci_term_i=a
	if(a!=0):
		hp.append(round(1/a,3))
	else:
		hp.append(a)
	for i in range(int(n-1)):
		reci_term_i+=d
		if(reci_term_i!=0):
			hp.append(round(1/reci_term_i,3))
		else:
			hp.append(reci_term_i)



	return hp	

