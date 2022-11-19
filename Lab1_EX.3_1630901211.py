def prime(L, R):

    for num in range(L , R + 1):
        if num >= 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=" ")
def Even(L, R):
    if (R < L):
        return

    if (R % 2 == 0):
        Even(L, R - 2)
    else:
        Even(L, R - 1)


    if (R % 2 == 0):
        print(R, end=" ")

def Odd(L, R):

    if (R < L):
        return

    if (R % 2 == 1):
        Odd(L, R - 2)
    else:
        Odd(L, R - 1)

    if (R % 2 == 1):
        print(R, end=" ")

if __name__ == '__main__':
    L = 1
    R = 11

    print("Even numbers:")
    Even(L, R)
    print()

    print("Odd numbers:")
    Odd(L, R)

    print("\nPrime numbers:")
    prime(L,R)


