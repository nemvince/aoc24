with open("input.txt") as f:
  data = f.read().splitlines()

directions = {
  "<": (0, -1),
  "^": (-1, 0),
  ">": (0, 1),
  "v": (1, 0)
}


def findGuard(grid):
  for i, row in enumerate(grid):
    for j, col in enumerate(row):  # noqa: VNE001
      if col in ["<", ">", "^", "v"]:
        return (i, j)


def part1(data):
  grid = [list(row) for row in data]
  guardX, guardY = findGuard(grid)
  dirX, dirY = directions[grid[guardX][guardY]]
  # check if the next position is within the grid
  while 0 <= guardX+dirX < len(grid) and 0 <= guardY+dirY < len(grid[0]):
    # check if next tile in our current direction is a #
    if grid[guardX+dirX][guardY+dirY] == "#":
      # turn right
      curDir = list(directions.keys())[(list(directions.values()).index((dirX, dirY)) + 1) % 4]
      dirX, dirY = directions[curDir]
    elif grid[guardX+dirX][guardY+dirY] == ".":
      guardX += dirX
      guardY += dirY
      grid[guardX][guardY] = "X"
    else:
      guardX += dirX
      guardY += dirY

  return sum([row.count("X") for row in grid])+1


def part2(data):
  grid = [list(row) for row in data]

  start_x = start_y = None
  start_direction = None
  for i in range(len(grid)):
    for j in range(len(grid[0])):  # noqa: VNE001
      if grid[i][j] in "^>v<":
        start_direction = grid[i][j]
        start_x, start_y = i, j
        break
    if start_direction:
      break

  if start_x is None or start_direction is None:
    raise ValueError("Starting position with direction not found in the grid.")

  dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
  turns = {"^": ">", ">": "v", "v": "<", "<": "^"}

  total = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):  # noqa: VNE001
      if (i == start_x and j == start_y) or grid[i][j] != ".":
        continue

      blocked = {(i, j)}

      pos = (start_x, start_y)
      direction = start_direction
      seen = set()
      loop_found = False

      while True:
        current_state = (pos, direction)
        if current_state in seen:
          loop_found = True
          break
        seen.add(current_state)

        dx, dy = dirs[direction]
        next_x = pos[0] + dx
        next_y = pos[1] + dy
        next_pos = (next_x, next_y)

        # Check boundary conditions
        if (next_x < 0 or next_x >= len(grid) or
            next_y < 0 or next_y >= len(grid[0])):
          break

        # Check if next position is blocked or a wall
        if next_pos in blocked or grid[next_x][next_y] == "#":
          direction = turns[direction]
        else:
          pos = next_pos

      # If loop is found, increment total
      if loop_found:
        total += 1

  return total


if __name__ == "__main__":
  print(part1(data))
  print(part2(data))
