def main():
    print("******Euclides*****")
    a = 1800
    b = 3240

    print("El máximo común divisor entre 180 y 324 es", mcd(a, b))


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


main()