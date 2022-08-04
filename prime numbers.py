
n = 20

#first creat range in which we want to find prime

number_range = set(range(2, n+1))
#create variable to which primes are saved
primes_list = []

#loop is required to run code again and again
while number_range:
    prime = number_range.pop()
    primes_list.append(prime)
    multiples= set(range(prime*2, n+1, prime))
    number_range.difference_update(multiples)
    
print(primes_list)
prime_count = len(primes_list)
largest_prime = max(primes_list)
smallest_prime = min(primes_list)
print("There are {prime_count} number of primes between 2 and {n}, and the largest prime nymber is {largest_prime}.")
