# Dog Age Calculater
# How old would your dog be if they were a human?


#1. Input:
sAge = input("What is your dogs age?")

#2. Convert Data:
fAge = float(sAge)

#3. Perform Calculation:
fHumanAge = fAge * 7.3

#4. Output:

print("The human age of your dog is: " + str(fHumanAge))
print("The human age of your dog (with formatting) is: " + format(fAge * 7.3,'.1f'))


## Less Lines of Code

# 1. Input:
# fAge = float( input("What is your dogs age? ") )
# print("The human age of your dog (with formatting) is: " + format(fAge * 7.3,'.1f'))

# 2. Input:
# print("The human age of your dog is: " + format( float ( input (What is your dogs age?" ) ) * 7.3, '.1f')

## Formatting
sDogName = input("What is your dogs name?")
# print( format(sDogName, "20") + format(fHumanAge, ".1f"))
# print( format(sDogName, ">20") + format (fHumanAge, "<.1f"))
# print( format (fHumanAge, "<.1f") + format(sDogName, ">20"))
