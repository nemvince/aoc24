import pathlib
import shutil
import sys

import cutie

import requests

YEAR = 2024


def getSessionToken():
  with open("session.txt", "r") as f:
    token = f.read().strip()
  if token == "":
    print("No session token found.")
    exit()
  return token


def fetchInput(year, day):
  token = getSessionToken()
  headers = {"Cookie": token}
  response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=headers)
  if response.status_code != 200:
    if response.text.startswith("Please don't repeatedly request this endpoint before it unlocks!"):
      print("Error: Input is not available yet.")
    elif response.status_code == 404:
      print("Error: Input not found.")
    else:
      print(f"Error: Could not connect to server, {response.text}")
    exit()
  return response.text


def getDay():
  day = cutie.get_number("Enter day: ")
  return str(int(day))


if __name__ == "__main__":
  day = getDay()
  inputData = fetchInput(YEAR, day)

  templateDir = pathlib.Path(__file__).parent.absolute()
  srcPath = templateDir.parent

  dayPath = srcPath / day
  if dayPath.exists():
    print(f"Error: Folder for day {day} already exists.")
    sys.exit(1)

  dayPath.mkdir()

  shutil.copy(templateDir / "template.py", dayPath / "main.py")

  with open(dayPath / "input.txt", "w") as f:
    f.write(inputData)

  with open(dayPath / "example.txt", "w") as f:
    f.write("")
