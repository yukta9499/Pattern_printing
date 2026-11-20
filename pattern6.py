print("right aligned triangle")
n = 5
for i in range(1,n+1):          #range for rows
    for j in range(n-i):            #loop for printing space
            print(" ",end = " ")
    for j in range(i):                  #loop for printing
            print("*", end = " ")

    print()
