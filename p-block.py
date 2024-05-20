# Функція для P-блоку (перестановка)
def p_box(input_bits):
    permute_order = [3, 1, 7, 5, 8, 6, 2, 4]
    output = "".join(input_bits[i - 1] for i in permute_order)
    return output

# Функція для зворотного P-блоку (перестановка)
def reverse_p_box(input_bits):
    reverse_permute_order = [2, 7, 1, 8, 4, 6, 3, 5]
    output = "".join(input_bits[i - 1] for i in reverse_permute_order)
    return output

if __name__ == "__main__":
    input_data = "01110011"
    p_result = p_box(input_data)
    print("P-блок прямого перетворення:", p_result)
    reverse_p_result = reverse_p_box(p_result)
    print("P-блок зворотного перетворення:", reverse_p_result)
