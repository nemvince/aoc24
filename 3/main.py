import re

with open("input.txt") as f:
  # one line of input
  data = f.read().strip()


def part1(data):
  pattern = r"mul\(\d{1,3},\d{1,3}\)"
  matches = re.findall(pattern, data)

  total = 0

  for match in matches:
    a, b = map(int, re.findall(r"\d+", match))  # noqa: VNE001
    total += a * b

  return total


def part2(data):
  pattern = r"mul\(\d{1,3},\d{1,3}\)"
  matches = re.findall(pattern, data)

  total = 0
  enable = True

  for match in matches:
    idx = data.index(match)
    before = data[:idx]
    doIdx, dontIdx = before.rfind("do()"), before.rfind("don't()")

    if doIdx + dontIdx != -2:
      enable = doIdx > dontIdx

    if enable:
      a, b = map(int, re.findall(r"\d+", match))  # noqa: VNE001
      total += a * b

  return total


if __name__ == "__main__":
  print(part1(data))
  print(part2(data))
