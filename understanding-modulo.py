"""making sense of modulo in python. When I started out, I used to struggle with understanding this operator, especially when it came to negative(-) numbers.
After a couple of research I discovered a trick which I am sharing here to save another person the trouble"""
"""
modulo(%) is the remainder when one number is divided by another number i.e.
x/y = z remainder r
we therefore can say;
x = y*z + r
r = x - y*z
where z is the mathematical floor value of x divide by y (integer division in python i.e. x//y). 
The complete equation then becomes
r = x - y*(floor(x/y))  NOTE ( = here is the mathematical equals not the assigment operator)
so x%y = x - y*(floor(x/y))
try with 1%2, -4%3, -1%60 (do it on paper then execute it in a code and see if you get same results)
modulo is very important especially in conversions..assume for example the time now is 23:00:00 and you minus 1 second.
How do you make the python code output 22:59:59?
"""
