# form: a * 4
def umfang_quadrat():
    a = input("insert a:\n")
    result = int(a) * 4
    print("Der Umfang beträgt: ", result)


# form: a ^ 2
def flaeche_quadrat():
    a = input("insert a:\n")
    result = int(a) ** 2
    print("Die Fläche beträgt: ", result)


# form: 2 * a + 2 * b = 2 (a + b)
def umfang_rechteck():
    a = input("insert a:\n")
    b = input("insert b:\n")
    result = 2 * (int(a) + int(b))
    print("Der Umfang beträgt: ", result)


# form: a * b
def flaeche_rechteck():
    a = input("insert a:\n")
    b = input("insert b:\n")
    result = int(a) * int(b)
    print("Die Fläche beträgt: ", result)


flaeche_rechteck()
