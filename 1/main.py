with open("input.txt") as f:
  d = f.read().splitlines()


def part1(data):
  data = [x.split("   ") for x in data]
  d1 = sorted([int(x[0]) for x in data])
  d2 = sorted([int(x[1]) for x in data])
  s = 0

  for i in range(len(d1)):
    s += abs(d1[i] - d2[i])

  return s


def part2(data):
  data = [x.split("   ") for x in data]
  d1 = sorted([int(x[0]) for x in data])
  d2 = sorted([int(x[1]) for x in data])

  s = 0

  for n in d1:
    app = d2.count(n)
    s += n * app

  return s


if __name__ == "__main__":
  print(part1(d))
  print(part2(d))
