def kinetic_energy(mass, velocity):
    energy = 0.5 * mass * (velocity ** 2)
    return energy
mass = float(input("Enter the mass in kg: "))
velocity = float(input("Enter the velocity in m/s: "))

result = kinetic_energy(mass, velocity)

print(f"The kinetic energy is: {result:.2f} Joules")