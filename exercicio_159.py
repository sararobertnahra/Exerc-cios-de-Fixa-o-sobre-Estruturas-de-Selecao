x = float(input("\ndigite valor de x: "))

if ((x > 4) or (x < -4)):
    fx = (5*x + 3) / ((x**2 - 16)**0.5)
    print(f"\nf(x)= {fx}")
else: print("\nNAO PODE SER FEITA")

print("\n")