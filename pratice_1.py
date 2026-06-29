class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def greet(customer):       ## this fucntion is our the class coz customer === cust so the cust.anme works here..
        print("hello",customer.name)
        

## pass by reference is happening here so if something another , that another will point that something...
##class object are also mutable datatype , that addrress only we can chnage the vlaue of teh varaible. (list , dict , set)


c1 = Customer("rishi",20)
c2 = Customer("ankit",87)
c3 = Customer("ram",9)

L = [c1,c2,c3]   ## collection of the objects ==> it can easily use as the simple list and simple commands
for i in L:
    print(i.age)
for i in L:
    print(i.name)