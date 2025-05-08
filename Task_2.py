import math

num = float(input("Enter a positive number: "))

if num <= 0:
    print("Please enter a number greater than 0.")

else:
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
    sin_val = math.sin(num)

print(f"\nResults for the number {num}:")
print(f"Square root: {sqrt_val}")
print(f"logarithm (ln): {log_val}")
print(f"Sine: {sin_val}")

