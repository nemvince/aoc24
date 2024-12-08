from collections import defaultdict

with open("input.txt") as f:
    data = [line.rstrip() for line in f]


def part1(data):
  antennaMap = dict()
  antennaTypes = defaultdict(list)
  for y, row in enumerate(data):  # noqa: VNE001
      for x, char in enumerate(row):  # noqa: VNE001
          antennaMap[(x, y)] = char
          if char != ".":
              antennaTypes[char].append((x, y))

  antinodes = set()
  for antennaType in antennaTypes:
      typeLen = len(antennaTypes[antennaType])

      for ant1Idx in range(0, typeLen - 1):
          first = antennaTypes[antennaType][ant1Idx]
          for ant2Idx in range(ant1Idx + 1, typeLen):
              second = antennaTypes[antennaType][ant2Idx]
              dx = first[0] - second[0]
              dy = first[1] - second[1]
              antinode1 = (first[0] + dx, first[1] + dy)
              antinode2 = (second[0] - dx, second[1] - dy)
              if antinode1 in antennaMap:
                  antinodes.add(antinode1)
              if antinode2 in antennaMap:
                  antinodes.add(antinode2)

  return len(antinodes)


def part2(data):
  yBound = len(data)
  xBound = 0
  antennaTypes = defaultdict(list)
  for y, row in enumerate(data):  # noqa: VNE001
      if not xBound:
          xBound = len(row)
      for x, char in enumerate(row):  # noqa: VNE001
          if char != ".":
              antennaTypes[char].append((x, y))

  antinodes = set()
  for antennaType in antennaTypes:
      typeLen = len(antennaTypes[antennaType])

      for ant1Idx in range(0, typeLen - 1):
          first = antennaTypes[antennaType][ant1Idx]
          for ant2Idx in range(ant1Idx + 1, typeLen):
              second = antennaTypes[antennaType][ant2Idx]
              antinodes.add(first)
              antinodes.add(second)
              fx, fy = first
              sx, sy = second
              dx = fx - sx
              dy = fy - sy
              while fx + dx in range(0, xBound) and fy + dy in range(0, yBound):
                  antinodes.add((fx + dx, fy + dy))
                  fx += dx
                  fy += dy
              while sx - dx in range(0, xBound) and sy - dy in range(0, yBound):
                  antinodes.add((sx - dx, sy - dy))
                  sx -= dx
                  sy -= dy

  return len(antinodes)


if __name__ == "__main__":
  print(part1(data))
  print(part2(data))
