saldomedio = float(input("\ndigite saldo medio: "))

if saldomedio < 501:
    credito = 0
elif saldomedio < 1001:
    credito = saldomedio*0.3
elif saldomedio < 3001:
    credito = saldomedio*0.4
else: credito = saldomedio*0.5

if credito != 0:
    print(f"\nComo seu saldo era de: {saldomedio}, seu credito sera de: {credito}")
else: (f"\nComo seu saldo era de: {saldomedio}, voce nao tera nenhum credito")

print("\n")