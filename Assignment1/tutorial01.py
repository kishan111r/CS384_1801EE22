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
	if(num2==0):
		return 0
	division = num1 / num2
	return division

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	#Power Logic
	power = 0	#By default we have to return 0 in case of any error



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
	gp=[]
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	return hp	

