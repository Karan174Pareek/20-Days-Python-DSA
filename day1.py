#program to find the area of the circle
pie=3.14159          #defining the value of pie
radius=float(input("enter the radius of the circle: "))     #taking the input from the user
area=pie*radius*radius
print("The area of the circle is: ",area)

#program to find the area of the square
length=float(input("Enter the side length of the square :"))  #taking input
area=length*length
print("the area of the square is:",area)

#program to find if the number is even or odd
number=int(input("ENETR A NUMBER TO FIND ODD OR EVEN:"))
if(number%2)==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")