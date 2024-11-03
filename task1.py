def caching_fibonacci():
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return n
        elif n == 1:
            return 1
        elif any(n == k for k in cache.keys()):
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


def main():
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))


if __name__ == "__main__":
    main()
