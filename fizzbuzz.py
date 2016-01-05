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
    num_list = []
    for num in range(1, end):
       num_list.append(fizzbuzz(num))
    return num_list

if __name__ == "__main__":
    import sys
    num_list = fizzbuzz_all(int(sys.argv[1]))
    for num in num_list:
        print(num)

