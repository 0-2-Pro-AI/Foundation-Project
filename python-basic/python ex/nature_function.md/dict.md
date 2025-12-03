function dictionary basically is use Hash Function and Bitwise and &

first, it hashing the word into a series of number

then use the function ("bitwise and" & ) to find the index

then take the info put in the number of the index

for example:

menu["pizza"]

hashing "pizza" into "123456789"(X)

size of dict is 8 = 2*3 (binary= 1000)

mask = size - 1 = 7 (binary = 0111), reverse of size, and the number of 1 is same with expotional of 2, in this case is 3

in language of computer, X is defined as binary (0,1)

and cause the expotional is 3

now the part of "and", 

computer will compare 3 last number of the mask and X

and just keep the value that both 1, others will be 0

in this case 
X = ....101 
mask = 0111

with the expotional 3, just compare 3 lasts number

and we have 101 = 5 

the exact index of X/8


So the pizza in the size number 5

And there is also many case that have the same size number 

Python use the memory organization mechanism( if the size number 5 is full, it will find the next nearest empty one)