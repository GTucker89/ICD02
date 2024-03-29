def first_3(x):
    if isinstance(x, str):
        length = len(x)
        return x[0:length:2]
    else:
        print("Error: input is not a string.")

print(first_3(34))
