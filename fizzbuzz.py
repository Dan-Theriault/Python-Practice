def fizzbuzz(num):
    for w in range(1, num):
        if (w % 5) == (w % 3) == 0:
            print("FizzBuzz")
        elif (w % 3) == 0:
            print("Fizz")
        elif (w % 5) == 0:
            print("Buzz")
        else:
            print(w)

if __name__ == "__main__":
    import sys
    fizzbuzz(int(sys.argv[1]))

