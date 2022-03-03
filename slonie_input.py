n = int(input())
mass = [int(x) for x in input().split()]
default = [int(x) - 1 for x in input().split()]
purpose = [int(x) - 1 for x in input().split()]

check = [False for x in range(n)]
elefants = [0 for x in range(n)]

min_mass = min(mass)
result = 0

for i in range(n):
    elefants[purpose[i]] = default[i]

for i in range(n):
    if not check[i]:
        min_mass_cycle = float('inf')
        len_cycle = 0
        sum_cycle = 0
        k = i
        while True:
            sum_cycle = sum_cycle + mass[k]
            min_mass_cycle = min(min_mass_cycle, mass[k])
            k = elefants[k]
            check[k] = True
            len_cycle = len_cycle + 1
            if k == i:
                break
        result = result + min(sum_cycle + (len_cycle - 2) * min_mass_cycle,
                              sum_cycle + min_mass_cycle + (len_cycle + 1) * min_mass)
print(result)
