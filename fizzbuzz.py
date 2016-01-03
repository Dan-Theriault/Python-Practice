def fizzbuzz(num):
    if (num % 3) == (num % 5) == 0:
        return 'FizzBuzz'
    elif (num % 3) == 0:
        return 'Fizz'
    elif (num % 5) == 0:
        return 'Buzz'
    else:
        return str(num)

def fizzbuzz_all(end):
    for num in range(1, end):
        print(fizzbuzz(num))

if __name__ == "__main__":
    import sys
    fizzbuzz_all(int(sys.argv[1]))

