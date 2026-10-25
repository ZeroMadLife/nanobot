def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # 生成器函数，生成斐波那契数列

# while True:
#     try:
#         #通过 next() 函数获取生成器的下一个值
#         print(next(f), end=" ")
#     except StopIteration:
#         break
for i in fibonacci(10):
    print(i, end=" ")