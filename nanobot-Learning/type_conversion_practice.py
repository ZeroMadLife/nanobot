"""练习：把字符串形式的订单数据转换成合适的 Python 类型。

运行方式：python nanobot-Learning/type_conversion_practice.py

先完成 convert_order() 中的 TODO，再运行文件检查结果。
变量名采用 snake_case，例如 order_id、unit_price。
"""

raw_order = {
    "order_id": "42",
    "unit_price": "12.50",
    "quantity": "3",
    "is_gift": "0",
    "tags": ["sale", "new", "sale"],
    "coordinates": ["厦门", "思明区"],
    "status_code": "65",
    "attributes": [("source", "website"), ("priority", "normal")],
}


def convert_order(order_data):
    """把原始订单转换成包含合适数据类型的新字典。"""
    converted_order = {}

    order_id = int(order_data["order_id"])
    unit_price = float(order_data["unit_price"])
    quantity = int(order_data["quantity"])
    status_code = int(order_data["status_code"])
    status_character = chr(status_code)

    converted_order = {
        "order_id": order_id,
        "unit_price": unit_price,
        "quantity": quantity,
        "subtotal": unit_price * quantity,
        "is_gift": bool(int(order_data["is_gift"])),
        "tags": set(order_data["tags"]),
        "coordinates": tuple(order_data["coordinates"]),
        "status_character": status_character,
        "status_code": ord(status_character),
        "attributes": dict(order_data["attributes"]),
        "order_id_binary": bin(order_id),
        "order_id_octal": oct(order_id),
        "order_id_hex": hex(order_id),
    }

    return converted_order


if __name__ == "__main__":
    result = convert_order(raw_order)
    for key, value in result.items():
        print(f"{key}: {value!r} ({type(value).__name__})")

    # 检查提示：order_id 应该是 int，unit_price 和 subtotal 是 float；
    # tags 是 set，coordinates 是 tuple，attributes 是 dict，is_gift 是 False。
    # status_character 应该是 'A'，order_id_binary 应该是 '0b101010'。
