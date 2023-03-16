
# CP : Code Postale

print("Stqrt")
CP = input("Code postale dqns lequel sera publie le texte : ")
nbCarac = input("nombre de caractere : ")
def getPrice(CP, nbCarac):
    print(CP)
    if CP in [2, 8, 7, 8, 26, 38, 60, 69,80 ,89]:
        print(0.189 * nbCarac)
    elif CP in [27, 76]:
        print(0.2 * nbCarac)
    elif CP in [59, 62,77,78,91,95]:
        print(0.221 * nbCarac)

    elif CP in [75,92,93,94]:
        print(0.232 * nbCarac)

    elif CP in [971, 972, 973, 977, 978, 986]:
        print(1.179 * nbCarac)

    elif CP in [974, 976]:
        print(0.204 * nbCarac)
    else:
        print (0.183 * nbCarac)

getPrice(CP, nbCarac)
