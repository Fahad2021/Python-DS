def myFun(*argv):
	for arg in argv:
		print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print("******************************************")
def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("******************************************")
# What is Python **kwargs
def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

print("******************************************")

# Using both *args and **kwargs to call a function
def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

print("******************************************************")
class car(): #defining car class
	def __init__(self,*args): #args receives unlimited no. of arguments as an array
		self.speed = args[0] #access args index like array does
		self.color=args[1]	
#creating objects of car class
audi=car(200,'red')
bmw=car(250,'black')
mb=car(190,'white')
	
print(audi.color)
print(bmw.speed)

