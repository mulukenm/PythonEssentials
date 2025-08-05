### Working with Numbers, Text, and Dates

import math

x = 625
print("The square root of", x, "is", math.sqrt(x))

# some functions from the Python Math Module
x1 = 60

print("The sine of", x1, "degrees is", math.sin(math.radians(x1)))
print("The cosine of", x1, "degrees is", math.cos(math.radians(x1)))
print("The tangent of", x1, "degrees is", math.tan(math.radians(x1)))

x2=1000
print("The value of pi is approximately", math.pi)
print("The logarithm of", x2, "to base 10 is", math.log10(x2))
print("The logarithm of", x2, "to base e is", math.log(x2))  
print("The logarithm of", 1000, "to base 10 is", math.log(1000, 10)) 
x3=5
print("The exponential of", x3, "is", math.exp(x3))             

greeting = "John"
print(f"Hello, {greeting}!" ) # Using f-string for formatted string literals

# Formatting numbers
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}")
print(f"Subtotal: ${quantity * unit_price:,.2f}")

# Percentage formatting
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")
print(f"Sales Tax Rate {sales_tax_rate:.2%}")

# Concatenating strings with formatting
first_name = "Alan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + middle_init + last_name
print(full_name)

print(f"{first_name} {middle_init}. {last_name}")

middle_init = " C "
full_name = first_name + middle_init + last_name
print(full_name)

# Calculating timespans
import datetime as dt
new_years_day = dt.date(2024, 1, 1)
memorial_day = dt.date(2024, 5, 27)
days_between = memorial_day - new_years_day
print(days_between)
print(type(days_between))