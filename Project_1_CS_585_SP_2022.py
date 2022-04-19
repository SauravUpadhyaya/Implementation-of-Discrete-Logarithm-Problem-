import time
def discreteLogarithm(b,z,n):

    for i in range(1,n): # loop executes for "n" times only
        k = b**i
        print(k)
        if(k%n == z):
            return(i)

b= int(input("Enter your value: "))
z = int(input("Enter your value: "))
n = int(input("Enter your value: "))

Starting_time = time.time()
TestCase = discreteLogarithm(b,z,n)
Ending_time = time.time()
print("In TestCase_1, value of b as {}, z as {} and n as {} is able to give solution when value of x is: {}".format(b, z, n, TestCase ))
print("It takes {} seconds to run TestCase_1".format(Ending_time - Starting_time))
