def print_matches(matchtext):
    print("Looking for",matchtext)
    while True:
        line=(yield)
        if matchtext in line:
            print(line)
matcher=[print_matches("python"),print_matches("pychan"),print_matches("jython")]
for m in matcher:
   next(m)