import re

with open("input.txt") as f:
  # one line of input
  d = f.read().strip()


def part1(data):
  pattern = r"mul\(\d{1,3},\d{1,3}\)"
  match = re.findall(pattern, data)

  s = 0

  for m in match:
    a, b = map(int, re.findall(r"\d+", m))
    s += a * b

  return s


def part2(data):
  pattern = r"mul\(\d{1,3},\d{1,3}\)"
  match = re.findall(pattern, data)

  s = 0
  en = True

  for m in match:
    idx = data.index(m)
    before = data[:idx]
    doIdx, dontIdx = before.rfind("do()"), before.rfind("don't()")

    if doIdx + dontIdx != -2:
      en = doIdx > dontIdx

    if en:
      a, b = map(int, re.findall(r"\d+", m))
      s += a * b

  return s


if __name__ == "__main__":
  print(part1(d))
  print(part2(d))
