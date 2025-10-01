#!/bin/zsh

YEAR=$1
DAY=$2

if [[ -z $YEAR ]] || [[ -z $DAY ]]; then
  echo "Usage: setup.sh <year> <day>"
  exit 1
fi

mkdir -p ~/dev/aoc/$YEAR/$DAY
cd ~/dev/aoc/$YEAR/$DAY

curl -s https://raw.githubusercontent.com/go-aoc/advent-of-code/master/2015/day$DAY/input.txt > data.txt
echo ```def partOne(input):
  print({input})

def partTwo(input):
  print({input})

if __name__ == "__main__":
  partOne("sample")
  partTwo("sample")
``` > main.py
