def fib(n):
    def fibonacci():
        a, b, c = 0, 1, 1
        for i in range(10000):
            yield a
            a, b, c = b, c, c + b

    numbers = list(fibonacci())
    even = [i for i in numbers if i % 2 == 0]
    data = even[0:n]
    print(data)

fib(7)
