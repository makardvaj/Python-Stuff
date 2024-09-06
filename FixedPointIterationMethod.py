import math
#g = lambds x : math.cbrt(math.sqrt(x) + 1)
g = lambda x : math.pow(math.e, 1/x)
guesses = [1]
diffs = []
print("\n\tx_n\t\t\tx_n+1\t\t\tx_n+1 - x_n")
for i in range(0, 20) :
  x_n = guesses[-1]  # The previous (last guess).
  x_n_plus_1 = g(x_n)
  guesses.append(x_n_plus_1)
  diffs.append(x_n_plus_1 - x_n)
  printf(f"{i}\t{guesses[i]}\t{guesses[i+1]}\t{diffs[i]}")
