def square_of_sequence(x):
    for i in range(x):
        yield i*i

gen=square_of_sequence(5)
while True:
    try:
        print("Received on next():",next(gen))
    except StopIteration:
        break
        