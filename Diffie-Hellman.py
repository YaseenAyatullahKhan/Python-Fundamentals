p = int(input("enter parameter p: "))
g = int(input("enter parameter g: "))
a = int(input("Person1 what's your secret key? "))
b = int(input("Person2 what's your secret key? "))
A = g^a % p
B = g^b % p
K1 = B^a % p
K2 = A^b % p
if K1 == K2:
    print("The generated keys match!")
else:
    print("The generated keys don't match!")