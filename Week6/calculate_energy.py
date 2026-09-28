def calculate_energy(mass):
    c = 2.99 * (10 ** 8)
    energy = mass * (c ** 2)
    return energy

mass = float(input("Enter the mass in kg: "))

energy = calculate_energy(mass)

print(f"The energy produced is: {energy:.2f} Joules")