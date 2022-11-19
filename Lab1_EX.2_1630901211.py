k = eval(input("Enter height of diamond:"))
def Diamond(k):
    for i in range(k):
        print(" " * (k-i),"X" * (2*i + 1))
    for i in range( k- 2, -1, -1):
        print(" " * (k - i),"X"*(2*i+1))

ip = int(input("enter the Diamonds length : "))
for i in range(0,ip):
    print("----------------------")
    Diamond(k)
    print("----------------------")





