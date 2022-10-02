"""
You need to find the smallest positive number that is evenly divisible by all of the numbers from 1 to N

sample input
2
3
10

sample output
6
2520
 """


def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        result = 2

        if n == 1:
            print(1)
        else:
            while True:
                # Create a list of numbers that goes from 1 to N with all false values
                numbers_to_divide = [False for i in range(n)]
                for i in range(n):
                    num = i + 1
                    if result % num == 0:
                        numbers_to_divide[i] = True
                if all(numbers_to_divide):
                    break
                else:
                    result += 1
            print(result)


if __name__ == "__main__":
    main()
