class MyIterator:
    # 返回迭代器对象本身
    def __iter__(self):
        self.a = 1
        return self
    # 通过 next() 方法返回下一个迭代器对象
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)