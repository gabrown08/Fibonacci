# Fibonacci number calculator by Greg Brown in 2019
# updated 2/1/2020

# not recursive
def fib(n):
  fib = [1, 1]
  while type(n) != type(1):
    try:
        n = int(n)
    except ValueError:
        print('error: the input was not an integer. enter an integer.')
        print()
        n = input('which Fibonacci Number do you desire? ')
  for i in range(n-1):
    fib.append(fib[i] + fib[i+1])
  # print(fib)
  print(f'F{n} is {fib[n-1]}')
  return fib[n-1]

# recursive function
def recFib(n):
  # print(n)
  if n <= 1:
    return n
  else:
    # print('*' * n)
    # print('*' * (recFib(n-1) + recFib(n-2)))
    return recFib(n-1) + recFib(n-2)

# recursive factorial
def factorial(n):
  # print(n)
  if n == 1:
    return n
  else:
    return(n*factorial(n-1))

# command prompt
while __name__ == '__main__':
  exec(input('>>>'))