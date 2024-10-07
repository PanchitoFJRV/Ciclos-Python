fibonacci = []

for i in range(21):
    if i < 2:
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    print(fibonacci[i])
