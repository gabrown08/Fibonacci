line = input('which Fibonacci Number do you desire? ')

fib = [1, 1]

for i in range(int(line) - 1):
  fib.append(fib[i] + fib[i + 1])
  
print('F' + str(line) + ' is ' + str(fib[int(line) - 1]))

input()
