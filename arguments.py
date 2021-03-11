#arguments adding two numbers.
def sum(x,y):
    a=x+y
    print("The sum is",a)
    sum(10,20)
    sum(501,958)
#multiplying two numbers
def product(x,y):
	a=x*y
	print("The product is",a)
	product(10,20)
	product(502,950)
#number of arguments
def courses(*args):
	for subject in args:
	 print(subject)
	 courses("big data", "ccna", "oop2")
def courses(*args):
	for subject in args:
	  return subject
	print(courses("Big data", "CCNA", "oop2","communuication"))
#arbitrary arguments
 def courses(**kwargs):
	for key,value in kwargs.items():
	    print("{}:{}" .format(key,value))
	    courses(first='big data',second='ccna',third='hcna')