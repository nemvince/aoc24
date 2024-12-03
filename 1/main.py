with open("input.txt") as f:
  data = f.read().splitlines()


def part1(data):
  data = [x.split("   ") for x in data]
  d1 = sorted([int(x[0]) for x in data])
  d2 = sorted([int(x[1]) for x in data])
  total = 0

  for i in range(len(d1)):
    total += d1[i] * d2[-i - 1]

  return total


def part2(data):
  data = [x.split("   ") for x in data]
  d1 = sorted([int(x[0]) for x in data])
  d2 = sorted([int(x[1]) for x in data])

  total = 0

  for locId in d1:
    app = d2.count(locId)
    total += locId * app

  return total


if __name__ == "__main__":
  print(part1(data))
  print(part2(data))
