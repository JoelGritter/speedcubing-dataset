import sys

first_line = True

with open("badCSV.csv", "r") as input_file:
    with open("goodCSV.csv", "a") as output_file:
        for line in input_file:
            if first_line:
                output_file.write("Number, Time, Scramble \n")
                first_line = False
                continue

            cur = line.strip().split(";")
            number = int(cur[0])
            time = cur[1]
            comment = cur[2]
            scramble = cur[3]
            date = cur[4]
            p1 = cur[5]

            output_file.write(str(number) + "," + time + "," + scramble + "\n")
