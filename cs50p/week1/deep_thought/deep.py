number = input("What's the answer to the Great Question of Life, the Universe, and Everything? ")
number = number.lower().strip()

if number in ("forty-two", "forty two") or int(number) == 42 or float(number) == 42.0:
    print("Yes")
else:
    print("No")