###### this is the second .py file ###########

####### write your code here ##########

#importing modules
import random
import math

#variable declarations
count = 0
j = 0

#generate and calculate the no of points that lies between the unitr circle
while ( j<100 ) :
	(X,Y)=(random.uniform(-1.0,1.0), random.uniform(-1.0,1.0))
	distance = math.sqrt(X*X + Y*Y)
	if (distance <= 1):
		count = count + 1
	j=j+1

#print the output on console
print 'No of points in the circle is : ',count
print 'Percentage of points in the circle is : ',count,'%'

