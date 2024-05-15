def umfang_quadrat():
    a = input("insert a:\n")
    result = int(a) * 4
    print("Der Umfang beträgt: ", result)


def flaeche_quadrat():
    a = input("insert a:\n")
    result = int(a) ** 2
    print("Die Fläche beträgt: ", result)


def umfang_rechteck():
    a = input("insert a:\n")
    b = input("insert b:\n")
    result = 2 * (int(a) + int(b))
    print("Der Umfang beträgt: ", result)


def flaeche_rechteck():
    a = input("insert a:\n")
    b = input("insert b:\n")
    result = int(a) * int(b)
    print("Die Fläche beträgt: ", result)


flaeche_rechteck()
