N = int(input("Enter the value of N:"))

prime_numbers = []
current_number = 2

while len(prime_numbers) < N:
    is_prime = True

    for i in range(2, int(current_number ** 0.5) + 1):
        if current_number % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(current_number)

    current_number += 1


print(f"The first {N} prime numbers are:")
for prime in prime_numbers:
    print(prime, end=" ")
