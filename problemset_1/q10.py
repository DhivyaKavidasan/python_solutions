<<<<<<< HEAD
'''
code snippet
submitted by : dhivya.kavidasan
date: 05/12/2017
'''
#a. What would the code above return if the statement x = 25 were replaced by x = -25?
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
  print 'low =', low, 'high =', high, 'ans =', ans
  numGuesses += 1
  if ans**2 < x:
    low = ans
  else:
    high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x

It results in infinite loop.


#b. What would have to be changed to make the code above for finding an approximation to the cube root of both negative and positive numbers?
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
  print 'low =', low, 'high =', high, 'ans =', ans
  numGuesses += 1
  if ans**3 < x:
    low = ans
  else:
    high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x



=======
'''
code snippet
submitted by : dhivya.kavidasan
date: 05/12/2017
'''
#a. What would the code above return if the statement x = 25 were replaced by x = -25?
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
  print 'low =', low, 'high =', high, 'ans =', ans
  numGuesses += 1
  if ans**2 < x:
    low = ans
  else:
    high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x

It results in infinite loop.


#b. What would have to be changed to make the code above for finding an approximation to the cube root of both negative and positive numbers?
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
  print 'low =', low, 'high =', high, 'ans =', ans
  numGuesses += 1
  if ans**3 < x:
    low = ans
  else:
    high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x



>>>>>>> 55b273e3ea4245b20f0dfcb26def4e1191e27510
