with open("input.txt") as f:
  data = f.read().splitlines()


def part1(grid):
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):  # noqa: VNE001
      if grid[i][j] != "X":
        continue

      if (
        i > 2 and j > 2 and
        grid[i - 1][j - 1] == "M" and
        grid[i - 2][j - 2] == "A" and
        grid[i - 3][j - 3] == "S"
      ):
          count += 1

      if (
        i > 2 and
        grid[i - 1][j] == "M" and
        grid[i - 2][j] == "A" and
        grid[i - 3][j] == "S"
      ):
          count += 1

      if (
        i > 2 and j < len(grid[i]) - 3 and
        grid[i - 1][j + 1] == "M" and
        grid[i - 2][j + 2] == "A" and
        grid[i - 3][j + 3] == "S"
      ):
          count += 1

      if (
        j > 2 and
        grid[i][j - 1] == "M" and
        grid[i][j - 2] == "A" and
        grid[i][j - 3] == "S"
      ):
          count += 1

      if (
        j < len(grid[i]) - 3 and
        grid[i][j + 1] == "M" and
        grid[i][j + 2] == "A" and
        grid[i][j + 3] == "S"
      ):
          count += 1

      if (
        i < len(grid) - 3 and j > 2 and
        grid[i + 1][j - 1] == "M" and
        grid[i + 2][j - 2] == "A" and
        grid[i + 3][j - 3] == "S"
      ):
          count += 1

      if (
        i < len(grid) - 3 and
        grid[i + 1][j] == "M" and
        grid[i + 2][j] == "A" and
        grid[i + 3][j] == "S"
      ):
          count += 1

      if (
        i < len(grid) - 3 and j < len(grid[i]) - 3 and
        grid[i + 1][j + 1] == "M" and
        grid[i + 2][j + 2] == "A" and
        grid[i + 3][j + 3] == "S"
      ):
          count += 1

  return count


def part2(grid):
  rows = len(grid)
  cols = len(grid[0])

  answers = ["MAS", "SAM"]

  count = 0

  for i in range(rows):
    for j in range(cols):  # noqa: VNE001
      c = grid[i][j]  # noqa: VNE001

      if (
        c != "A" or
        i - 1 < 0 or
        i + 1 >= rows or
        j - 1 < 0 or
        j + 1 >= cols
      ):
        continue

      topL, topR = grid[i - 1][j - 1], grid[i - 1][j + 1]
      botL, botR = grid[i + 1][j - 1], grid[i + 1][j + 1]

      diagonal1 = topL + c + botR
      diagonal2 = topR + c + botL

      if diagonal1 in answers and diagonal2 in answers:
        count += 1

  return count


if __name__ == "__main__":
  print(part1(data))
  print(part2(data))
