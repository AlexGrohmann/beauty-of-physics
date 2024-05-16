def calculate_force(mass, acceleration):
    return mass * acceleration


def calculate_mass(force, acceleration):
    return force / acceleration


def calculate_acceleration(force, mass):
    return force / mass


def main():
    print("Welcome to the force calculator!")

    known_values = input(
        "Which two values do you have? (mass, acceleration, force): "
    ).split()

    if len(known_values) != 2:
        print("Please input exactly two values.")
        return

    known_values = [value.lower() for value in known_values]

    if "mass" in known_values and "acceleration" in known_values:
        mass = float(input("Enter the value of mass (in kg): "))
        acceleration = float(input("Enter the value of acceleration (in m/s^2): "))
        force = calculate_force(mass, acceleration)
        print("The force is: {:.2f} N".format(force))

    elif "mass" in known_values and "force" in known_values:
        mass = float(input("Enter the value of mass (in kg): "))
        force = float(input("Enter the value of force (in N): "))
        acceleration = calculate_acceleration(force, mass)
        print("The acceleration is: {:.2f} m/s^2".format(acceleration))

    elif "acceleration" in known_values and "force" in known_values:
        acceleration = float(input("Enter the value of acceleration (in m/s^2): "))
        force = float(input("Enter the value of force (in N): "))
        mass = calculate_mass(force, acceleration)
        print("The mass is: {:.2f} kg".format(mass))

    else:
        print("Invalid combination of values.")


if __name__ == "__main__":
    main()
