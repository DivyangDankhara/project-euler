# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


num = int(input())
def largest_prime_factor(n):
  ans = 0
  while n % 2 ==0:
    n /= 2
    ans = 2

  div = 3
  while n != 1 and div <= n:
    if n % div == 0:
      n /= div
      ans = div
    else:
      div +=2
  return ans

print(largest_prime_factor(num))
