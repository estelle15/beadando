def max_prime(number):
  factor=2:
    while factor*factor<=number:
      while number%factor==0:
        number/=factor
      factor+=1
    if (number>1):
      return number
   return factor


print max_prime(5)
print max_prime(7)
print max_prime(13)
print max_prime(29)
print max_prime(600851475143)
