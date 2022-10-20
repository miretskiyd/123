def zadanie3(n):
    r = 0
    while n > 0:
        r = (r*10) + (n % 10)
        n //= 10
    return r
print(zadanie3(int(input("Введите число: "))))
