# (i) Add 50 and 60 to L
L = [11, 12, 13, 14]
L.append(50)
L.append(60)
print("After adding 50 and 60:", L)

# (ii) Remove 11 and 13 from L
L.remove(11)
L.remove(13)
print("After removing 11 and 13:", L)

# (iii) Sort L in ascending order
L.sort()
print("Sorted in ascending order:", L)

# (iv) Sort L in descending order
L.sort(reverse=True)
print("Sorted in descending order:", L)

# (v) Search for 13 in L
if 13 in L:
    print("13 is found in the list.")
else:
    print("13 is not found in the list.")

# (vi) Count the number of elements present in L
count = len(L)
print("Number of elements in the list:", count)

# (vii) Sum all the elements in L
total_sum = sum(L)
print("Sum of all elements:", total_sum)

# (viii) Sum all ODD numbers in L
odd_sum = sum([num for num in L if num % 2 != 0])
print("Sum of odd numbers:", odd_sum)

# (ix) Sum all EVEN numbers in L
even_sum = sum([num for num in L if num % 2 == 0])
print("Sum of even numbers:", even_sum)

# (x) Sum all PRIME numbers in L
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_sum = sum([num for num in L if is_prime(num)])
print("Sum of prime numbers:", prime_sum)

# (xi) Clear all the elements in L
L.clear()
print("List after clearing all elements:", L)

# (xii) Delete L
del L
print("List deleted.")
