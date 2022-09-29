# Complex Numbers 
# complex() function returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the function serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

complex1 = "32+2j"
print(complex(complex1))

print(complex(2, 3))
