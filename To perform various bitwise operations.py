#Write a Python program to perform various bitwise operations
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print("Value of A:",a)
print("Value of B:",b)
print("Result of Bitwise AND=",(a&b))
print("Result of Bitwise OR=",(a|b))
print("Result of Bitwise EXOR=",(a^b))
print("Result of Bitwise NOT=",~(a|b))
print("Result of Bitwise LeftShift=",(a<<b))
print("Result of Bitwise RightShift=",(a>>b))

