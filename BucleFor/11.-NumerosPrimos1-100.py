print("Los números primos son:")
primos = []

for i in range(2, 101):
    es_primo = True
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(i)

print(primos)
