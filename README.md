# speedcubing-dataset

## What is this?
One of my hobbies is [speedcubing](https://en.wikipedia.org/wiki/Speedcubing). This sport(?) involves solving a Rubik's cube as quickly as possible.

While I am not a world-class speedcuber, I do have a lot of experience. This dataset represents a practice session that I've continued to use from roughly May 2018 - December 2020, with just over 50k datapoints. (All representing regular 3x3 Rubik's cube solves)

To my knowledge, there doesn't exist a large dataset for speedcubing yet. So I thought I'd put this out there to change that.

Solves were executed as closely as possible to the [WCA Regulations](https://www.worldcubeassociation.org/regulations/), including +2 penalties and DNFs. 

Note that these penalties mean that you can't just parse the times as floats, since there may be strings. '+' is appended to a time that has a penalty added to the time, 'DNF' will appear for any solves that were disqualified.

## The Data Files:
- `badCSV.csv` -> the csv file provided by cstimer
  - Separated by semicolons
  - Contains number, time, comment, scramble, date, and p1
- `goodCSV.csv` -> the csv file I parsed
  - Separated by commas
  - Contains number, time, and scramble

## The Code:
- `csv_fixer.py` -> parses `badCSV.csv` into `goodCSV.csv`

## Data Overview:
- single
    - best: 7.70
    - worst: 36.39

best mean of 3: 10.49 (σ = 0.81)

best avg of 5: 11.14 (σ = 0.76)

best avg of 12: 12.12 (σ = 0.94)

best avg of 25: 12.46 (σ = 1.26)

best avg of 50: 12.60 (σ = 1.15)

best avg of 100: 13.13 (σ = 1.19)

best avg of 200: 13.29 (σ = 1.12)

best avg of 500: 13.49 (σ = 1.21)

best avg of 1000: 13.61 (σ = 1.24)

best avg of 2000: best: 13.71 (σ = 1.27)

best avg of 5000: best: 13.91 (σ = 1.29)

best avg of 10000: best: 14.02 (σ = 1.33)

Average: 14.85 (σ = 1.53)
Mean: 14.95
