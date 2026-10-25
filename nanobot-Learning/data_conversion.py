"""练习：把接口返回的商品数据整理成方便展示的格式。

运行方式：python nanobot-Learning/data_conversion.py

练习目标：遍历 list、读取 dict、做类型转换、筛选数据并生成新 list。
先根据 TODO 自己补全，再对照末尾的预期结果检查。
"""

# 模拟从接口拿到的数据。接口常把数字也作为字符串传回来。
raw_products = [
    {"id": "101", "name": "键盘", "price": "199.9", "stock": "12"},
    {"id": "102", "name": "鼠标", "price": "79.5", "stock": "0"},
    {"id": "103", "name": "显示器", "price": "899", "stock": "5"},
]


def convert_products(products):
    """返回转换后的商品列表，只保留有库存的商品。"""
    converted = []

    # TODO 1：遍历 products 中的每个商品字典。
    # TODO 2：把 id、stock 转成 int，把 price 转成 float。
    for product in products:
        converted_product = {
            "id": int(product["id"]),
            "name": product["name"],
            "price": float(product["price"]),
            "stock": int(product["stock"]),
            "in_stock": True
        }
        if converted_product["stock"] > 0:
            converted.append(converted_product)
    # TODO 3：只保留 stock 大于 0 的商品。
    # TODO 4：创建新字典，字段为 id、name、price、stock、in_stock。
    #         in_stock 的值设为 True。
    
    # TODO 5：把新字典添加到 converted，最后 return converted。

    return converted


if __name__ == "__main__":
    result = convert_products(raw_products)
    for product in result:
        print(product)

    # 预期：有两行，分别是键盘和显示器；鼠标库存为 0，因此被筛掉。
    # {'id': 101, 'name': '键盘', 'price': 199.9, 'stock': 12, 'in_stock': True}
    # {'id': 103, 'name': '显示器', 'price': 899.0, 'stock': 5, 'in_stock': True}
