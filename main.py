def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # Check divisibility up to square root
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to the given limit."""
    is_prime = [True] * (limit + 1) # Assume all numbers up to limit are prime
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False # Mark multiples of p as not prime
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]  # Return all primes


def get_prime_pairs(number):
    if number % 2 == 1 and number != 2:
        return []  # Odd numbers (except 2) can't be written as the sum of two primes
    primes = sieve_of_eratosthenes(number)
    print(primes)
    sum_of_two_primes = set()
    for prime in primes:
        complement = number - prime
        if complement >= prime and is_prime(complement):
            sum_of_two_primes.add((prime, complement))
    if not sum_of_two_primes:
        print(f"No pairs of primes found that sum to {number}.")
    else:
        return sum_of_two_primes


def print_prime_pairs(number, prime_pairs):
    """Prints the prime pairs in a readable format."""
    if not prime_pairs:
        print(f"No pairs of primes found that sum to {number}.")
    else:
        for pair in prime_pairs:
            print(f"The number {number} equals the sum of {pair[0]} and {pair[1]}.")

def main():
    while True:
        try:
            number = int(input("Enter a number:"))
            prime_pairs = get_prime_pairs(number)
            print_prime_pairs(number, prime_pairs)
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
