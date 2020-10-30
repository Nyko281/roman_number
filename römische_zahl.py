numbers = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

x = input("Römische Zahl eingeben: ")

z = 0
previous_value = 0

for char in x:
    if char in numbers: 
        if numbers[char] > previous_value:
            z -= previous_value
        else:
            z += previous_value
    else:
        print("Keine römische Zahl")
        exit()
    previous_value = numbers[char]
z += previous_value
print("Ergebnis: " + str(z))


