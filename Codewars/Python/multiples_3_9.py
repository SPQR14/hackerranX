def solution(number):
    return sum([x for x in range(1, number) if x % 3 == 0 or x % 5 == 0])

pruebas = {
    3 : 3,
    6 : 8,
    16 : 60,
    15 : 45,
    200 : 9168
}

passed = 0

for i in pruebas:
    if (solution(i) == pruebas.get(i)):
        passed += 1

print(f'Total passed: {passed} out of {len(pruebas)}')