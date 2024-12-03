with open("input.txt") as f:
  data = f.read().splitlines()


def isSafe(level):
  if level != sorted(level) and level != sorted(level, reverse=True):
    return False

  for i in range(len(level) - 1):
    if abs(level[i] - level[i + 1]) < 1 or abs(level[i] - level[i + 1]) > 3:
      return False

  return True


def part1(data):
  data = [x.split(" ") for x in data]
  total = 0

  for level in data:
    level = [int(x) for x in level]
    total += isSafe(level)

  return total


def part2(data):
  data = [x.split(" ") for x in data]
  total = 0

  for level in data:
    level = [int(x) for x in level]
    if isSafe(level):
      total += 1
      continue

    for i in range(len(level)):
      test = level[:i] + level[i + 1:]
      if isSafe(test):
        total += 1
        break

  return total


if __name__ == "__main__":
  print(part1(data))
  print(part2(data))
