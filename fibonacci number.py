#Fibonacci number calculator by Greg Brown in 2019

n = input('which Fibonacci Number do you desire? ')

while type(n) != type(1):
    try:
        n = int(n)
    except ValueError:
        print('error: the input was not an integer. enter an integer.')
        print()
        n = input('which Fibonacci Number do you desire? ')

fib = [1, 1]

for i in range(int(n) - 1):
  fib.append(fib[i] + fib[i + 1])
  
print('F' + str(n) + ' is ' + str(fib[int(n) - 1]))

input()
