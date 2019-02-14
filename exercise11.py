# Let's do our own Bitmaker version of FizzBuzz, which is the name of a classic job interview coding problem.
#
# Write a program that loops over the numbers from 1 to 100.
# If the number is a multiple of three, output the string "Bit". For multiples of five, output "Maker".
# For numbers which are multiples of both three and five, output "BitMaker".
# Otherwise output the number itself.
#--------------------------------------------------------------------------------------------------------------
def bit_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("BitMaker")
        elif i % 3 == 0:
            print("Bit")
        elif i % 5 == 0:
            print("Maker")
        else:
            print(i)
    return

bit_buzz()



#--------------------------------------------------------------------------------------------------------------
