'''
Q1. L is a list defined as L= [11, 12, 13, 14].
(i) WAP to add 50 and 60 to L. 
(ii) WAP to remove 11 and 13from L.
(iii) WAP to sort L in ascending order.
(iv) WAP to sort L in descending order.
(v) WAP to search for 13 in L.
(vi) WAP to count the number of elements present in L.
(vii) WAP to sum all the elements in L.
(viii) WAP to sum all ODD numbers in L.
(ix) WAP to sum all EVEN numbers in L.
(x) WAP to sum all PRIME numbers in L.
(xi) WAP to clear all the elements in L.
(xii) WAP to delete L.
'''

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

'''Q2. D is a dictionary defined as D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}.
(i) WAP to add new entry in D; key=8 and value is 8.8
(ii) WAP to remove key=2.
(iii) WAP to check weather 6 key is present in D.
(iv) WAP to count the number of elements present in D.
(v) WAP to add all the values present D.
(vi) WAP to update the value of 3 to 7.1.
(vii) WAP to clear the dictionary.

'''
# (i) Add new entry in D: key=8, value=8.8
D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}
D[8] = 8.8
print("After adding new entry:", D)

# (ii) Remove key=2 from D
del D[2]
print("After removing key=2:", D)

# (iii) Check whether key=6 is present in D
if 6 in D:
    print("Key=6 is present in the dictionary.")
else:
    print("Key=6 is not present in the dictionary.")

# (iv) Count the number of elements present in D
count = len(D)
print("Number of elements in the dictionary:", count)

# (v) Add all the values present in D
values_sum = sum(D.values())
print("Sum of all values:", values_sum)

# (vi) Update the value of key=3 to 7.1
D[3] = 7.1
print("After updating value of key=3:", D)

# (vii) Clear the dictionary
D.clear()
print("Dictionary after clearing:", D)

'''Q3. S1 is a set defined as S1= [10, 20, 30, 40, 50, 60].
 S2 is a set defined as S2= [40, 50, 60, 70, 80, 90].
(i) WAP to add 55 and 66 in Set S1.
(ii) WAP to remove 10 and 30 from Set S1.
(iii) WAP to check whether 40 is present in S1.
(iv) WAP to find the union between S1 and S2.
(v) WAP to find the intersection between S1 and S2.
(vi) WAP to find the S1 - S2.
'''
# (i) Add 55 and 66 to Set S1
S1 = {10, 20, 30, 40, 50, 60}
S1.add(55)
S1.add(66)
print("After adding 55 and 66 to S1:", S1)

# (ii) Remove 10 and 30 from Set S1
S1.remove(10)
S1.remove(30)
print("After removing 10 and 30 from S1:", S1)

# (iii) Check whether 40 is present in S1
if 40 in S1:
    print("40 is present in S1.")
else:
    print("40 is not present in S1.")

# (iv) Find the union between S1 and S2
S2 = {40, 50, 60, 70, 80, 90}
union_set = S1.union(S2)
print("Union of S1 and S2:", union_set)

# (v) Find the intersection between S1 and S2
intersection_set = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection_set)

# (vi) Find S1 - S2 (elements in S1 but not in S2)
difference_set = S1.difference(S2)
print("Elements in S1 but not in S2:", difference_set)
'''Q4. Write the following program.
(i) WAP to print 100 random strings whose length between 6 and 8.
(ii) WAP to print all prime numbers between 600 and 800.
(iii) WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.

'''
import random
import string

# (i) Print 100 random strings whose length is between 6 and 8
for _ in range(100):
    string_length = random.randint(6, 8)
    random_string = ''.join(random.choices(string.ascii_letters, k=string_length))
    print(random_string)

# (ii) Print all prime numbers between 600 and 800
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(600, 801):
    if is_prime(num):
        print(num)

# (iii) Print all numbers between 100 and 1000 that are divisible by 7 and 9
for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num)
        '''Q5. WAP to create two lists of 10 random numbers between 10 and 30; Find 
(i) Common numbers in the two lists
(ii) Unique numbers in both the list
(iii) Minimum in both the list
(iv) Maximum in both the list
(v) Sum of both the lists
Q6. WAP to create a list of 100 random numbers between 100 and 900. Count and print the: 
(i) All odd numbers
(ii) All even numbers
(iii) All prime numbers
Q7. D is a dictionary defined as D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}. 
 WAP to read all the keys and values from dictionary and write to the file in the given below format.
Key1, Value1
Key2, Value2
Key3, Value3
Q8. L is a list defined as L={"One","Two","Three","Four","Five"}.
 WAP to count the length of reach element from a list and write to the file in the given below format:
One, 3
Two, 3
Four, 4
Q9. Write to the file 100 random strings whose length between 10 and 15.
Q10. Write to the file all prime numbers between 600 and 800.
Q11. WAP to calculate the time taken by a program
        '''
import random

# Create two lists of 10 random numbers between 10 and 30
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)

# (i) Common numbers in the two lists
common_numbers = list(set(list1) & set(list2))
print("Common numbers:", common_numbers)

# (ii) Unique numbers in both lists
unique_numbers = list(set(list1) ^ set(list2))
print("Unique numbers:", unique_numbers)

# (iii) Minimum in both lists
min_value = min(min(list1), min(list2))
print("Minimum value:", min_value)

# (iv) Maximum in both lists
max_value = max(max(list1), max(list2))
print("Maximum value:", max_value)

# (v) Sum of both lists
total_sum = sum(list1) + sum(list2)
print("Sum of both lists:", total_sum)

# Q6. WAP to create a list of 100 random numbers between 100 and 900. Count and print the:
import random

# Create a list of 100 random numbers between 100 and 900
random_numbers = random.sample(range(100, 901), 100)

# (i) All odd numbers
odd_numbers = [num for num in random_numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)

# (ii) All even numbers
even_numbers = [num for num in random_numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# (iii) All prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in random_numbers if is_prime(num)]
print("Prime numbers:", prime_numbers)

# Q7. D is a dictionary defined as D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}.
# D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

with open("dictionary_output.txt", "w") as file:
    for key, value in D.items():
        file.write(f"{key}, {value}\n")

        # Q8. L is a list defined as L={"One","Two","Three","Four","Five"}.
        # L = {"One", "Two", "Three", "Four", "Five"}
        L = ["One", "Two", "Three", "Four", "Five"]

with open("length_output.txt", "w") as file:
    for element in L:
        file.write(f"{element}, {len(element)}\n")
        #9. Write to the file 100 random strings whose length between 10 and 15.
        import random
import string

with open("random_strings.txt", "w") as file:
    for _ in range(100):
        string_length = random.randint(10, 15)
        random_string = ''.join(random.choices(string.ascii_letters, k=string_length))


     

