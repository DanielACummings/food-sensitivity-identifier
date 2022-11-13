class Log:
    def __init__(self, lines) -> None:
        self.lines = lines


# Get log from user
inputFile = input('Enter path to .csv log file: ')

# Enter raw log data into Log class
with open(inputFile, 'r') as f:
    lines = f.readlines()

# Instantiate Log class
log = Log(lines)

# test
for line in log.lines:
    print(line, end='')
input('done')
#
