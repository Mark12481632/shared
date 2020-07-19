
def create_primes(count: int):  
  def is_prime(num, primes):
    for p in primes:
      if num % p == 0:
        return False
    return True

  def next_prime(primes):  
    new_num = primes[-1] + 1
    while not is_prime(new_num, primes):
      new_num += 1
    return new_num

  primes = [2]
  while len(primes) < count:
    prime = next_prime(primes)
    primes.append(prime)
  return primes

print(create_primes(5000))
