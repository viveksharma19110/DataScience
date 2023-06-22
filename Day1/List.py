L= [11, 12, 13, 14]

L.append(50)
L.append(60)


L.remove(11)
L.remove(13)


L.sort()

L.sort(reverse=True)


if 13 in L:
    print("13 is present in L")
else:
    print("13 is not present in L")


len(L)


sum(L)


sum([x for x in L if x % 2 == 1])


sum([x for x in L if x % 2 == 0])


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum([x for x in L if is_prime(x)])


L.clear()


del L