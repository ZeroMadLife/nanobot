def reverse(input):
    inputWords = input.split(" ")
    # 第三个是指从后往前取元素 从拆分的list中
    inputWords = inputWords[-1::-1]

    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    # input = "I like runoob"
    # rw = reverse(input)
    # print(rw)

    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

    if "AAA" in sites:
        print("Runoob 在集合中")
    else:
        print("Runoob 不在集合中")

    # set 可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')

    print(a)
    print(a - b)  # a 和 b 的差集
    print(a | b)  # a 和 b 的并集
    print(a & b)  # a 和 b 的交集
    print(a ^ b)  # a 和 b 的对称差分