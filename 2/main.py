with open("input.txt") as f:
  d = f.read().splitlines()


def isSafe(level):
  if level != sorted(level) and level != sorted(level, reverse=True):
    return False

  for i in range(len(level) - 1):
    if abs(level[i] - level[i + 1]) < 1 or abs(level[i] - level[i + 1]) > 3:
      return False

  return True


def part1(data):
  d = [x.split(" ") for x in data]
  s = 0

  for level in d:
    level = [int(x) for x in level]
    s += isSafe(level)

  return s


def part2(data):
  d = [x.split(" ") for x in data]
  s = 0

  for level in d:
    level = [int(x) for x in level]
    if isSafe(level):
      s += 1
      continue

    for i in range(len(level)):
      test = level[:i] + level[i + 1:]
      if isSafe(test):
        s += 1
        break

  return s


if __name__ == "__main__":
  print(part1(d))
  print(part2(d))
