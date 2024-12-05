with open("input.txt") as f:
  data = f.read().split("\n\n")

orderingRules = [x.split("|") for x in data[0].splitlines()]
updateNumbers = [x.split(",") for x in data[1].splitlines()]


def isValid(update, rule):
  if rule[0] in update and rule[1] in update:
    if update.index(rule[0]) > update.index(rule[1]):
      return False

  return True


def part1(data):
  validUpdates = []
  for update in updateNumbers:
    valid = True
    for rule in orderingRules:
      if not isValid(update, rule):
        valid = False

    if valid:
      validUpdates.append(update)

  middleNumbers = [int(update[int(len(update)/2)]) for update in validUpdates]

  return sum(middleNumbers)


def part2(data):
  invalidUpdates = []
  for update in updateNumbers:
    valid = True
    for rule in orderingRules:
      if not isValid(update, rule):
        valid = False

    if not valid:
      invalidUpdates.append(update)

  for update in invalidUpdates:
    while not all([isValid(update, rule) for rule in orderingRules]):
      for rule in orderingRules:
        if not isValid(update, rule):
          idx0 = update.index(rule[0])
          idx1 = update.index(rule[1])

          update.insert(idx0, update.pop(idx1))

  middleNumbers = [int(update[int(len(update)/2)]) for update in invalidUpdates]

  return sum(middleNumbers)


if __name__ == "__main__":
  print(part1(data))
  print(part2(data))
