""" 
Created By SORENSHAMLOU

Create At : 2024/10/17

Update At : 2024/10/17

File Name : main.py

Version : 1.1.1
"""


from colorama import Fore

from numpy import (
    zeros,
    int32
)
def print_square(rc):
    count = 1
    array = zeros(
        (rc,rc),
        dtype = int32
    )
    if rc%2 == 1:
        i = 0
        j = rc//2
        array[i][j] = count

        count+=1
        while count<=rc*rc:
            x = i-1
            y = j+1


            # Validators
            if x<0 and y==rc:
              x=i+i,
              y=j
            
            elif x<0:
                x=rc-1
                i=x
            
            elif y==rc:
                y=0
                j=y
            
            if array[x][y] != 0:
                x=i+1
                y=j
            
            # set value
            array[x][y] = count

            i=x
            j=y

            count+=1
        
        for i in array:
            row_sum = 0
            for j in i:
                print(f"{Fore.LIGHTMAGENTA_EX} {j}", end="\t")
                row_sum+=j
            else:
                print(f"{Fore.WHITE}👉  {row_sum}", end=" ")
            print("\n\n")
        else:
            for i in array:
                print(f"{Fore.WHITE}👇", end="\t")
            print("\n\n")
            for i in array:
                print(f"{Fore.WHITE}{row_sum}", end="\t")
    else:
        print(f"{Fore.RED} Error: Number is not Odd")
    


try:
    rc = int(
        input(
            f"{Fore.GREEN} Enter Number Of Row And Col >>> {Fore.CYAN}"
        )
    )
except ValueError:
    print(f"{Fore.RED} Error : Value Error")
    exit(0)

print_square(rc)
