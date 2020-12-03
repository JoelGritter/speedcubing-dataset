# speedcubing-dataset

## The Data:
- `badCSV.csv` -> the csv file provided by cstimer
  - Separated by semicolons
  - Contains number, time, comment, scramble, date, and p1
- `goodCSV.csv` -> the csv file I parsed
  - Separated by commas
  - Contains number, time, and scramble

## The Code:
- `csv_fixer.py` -> parses `badCSV.csv` into `goodCSV.csv`
