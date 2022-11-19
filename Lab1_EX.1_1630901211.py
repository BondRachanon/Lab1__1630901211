k = eval(input("Enter height of diamond:"))
for i in range(k):
    print(" " * (k-i),"X" * (2*i + 1))
for i in range( k- 2, -1, -1):
    print(" " * (k - i),"X"*(2*i+1))



