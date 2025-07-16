def div42By(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: you cannot divide by zero')


print(div42By(2))
print(div42By(5))
print(div42By(0))
print(div42By(6))
