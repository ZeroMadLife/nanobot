def calculate_is_valid_identifier(identifier: str):
    try:
        exec(f"{identifier} = None")
        return True
    except:
        return False

print(calculate_is_valid_identifier("valid_identifier"))  # True
print(calculate_is_valid_identifier("1invalid_identifier"))  # False