x = int(input("how many lines?"))
for q in range(x, 0, -1):
    print(" " * (x - q), end="")
    print("&" * (2 * q - 1))
