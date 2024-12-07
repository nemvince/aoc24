import itertools
from multiprocessing import Pool, cpu_count

with open("input.txt") as f:
  data = f.read().splitlines()


def evaluate_expression(numbers, operators):
  result = numbers[0]
  for i in range(len(operators)):
    if operators[i] == "+":
      result += numbers[i + 1]
    elif operators[i] == "*":
      result *= numbers[i + 1]
    elif operators[i] == "||":
      result = int(str(result) + str(numbers[i + 1]))
  return result


def generate_operators(length, operators):
  return list(itertools.product(operators, repeat=length - 1))


def solve_line(line, operators):
  testValue, numbers = line.split(": ")
  testValue = int(testValue)
  numbers = list(map(int, numbers.split(" ")))

  operators = generate_operators(len(numbers), operators)

  for op in operators:
    if evaluate_expression(numbers, op) == testValue:
      return testValue
  return 0


def solve(data, operators):
  with Pool(processes=cpu_count()) as pool:
    results = pool.starmap(solve_line, [(line, operators) for line in data])
  return sum(results)


if __name__ == "__main__":
  print(solve(data, ["+", "*"]))
  print(solve(data, ["||", "+", "*"]))
