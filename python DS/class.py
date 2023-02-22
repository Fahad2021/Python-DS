class Dog:
    def __init__(self,_name,_age,_color):
        self.name = _name
        self.age = _age
        self.color = _color
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_color(self):
        return self.color
    def bark(self):
        print("Gheo Gheo Gheo")
mydogobj=Dog("Bag",2,"Red")
mydogobj.bark()
print(mydogobj.get_name())
print(mydogobj.get_age())
print(mydogobj.get_color())


class Man:
    def __init__(self,_fname,_lname,_age):
        self.fname=_fname
        self.lname=_lname
        self.age=_age

    def get_fname(self):
        return "Tar first nam"+" "+self.fname
    def get_lname(self):
        return "Tar ses nam"+" "+ self.lname
    def get_age(self):
        return "Tar boyos"+" " +str(self.age) +" "+"bosor"
    def describe(self):
        print("he is"+" "+self.fname)

myMan=Man("Fahad","Rahman",2)
myMan.describe()
print(myMan.get_fname())
print(myMan.get_lname())
print(myMan.get_age())

# argv ,*argv in python

def myFun(*argv):
	for arg in argv:
		print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')










