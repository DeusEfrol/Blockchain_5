# Таблиця замін для S-блоку
S_BOX = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 6, 1, 13, 4, 10, 7, 0, 11],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

# Функція для S-блоку
def s_box(input_bits):
    input1 = input_bits[:4]  # Перші 4 біти
    input2 = input_bits[4:]  # Останні 4 біти

    row1 = int(input1[0] + input1[3], 2)  # Визначення рядка для першої тетради
    col1 = int(input1[1:3], 2)  # Визначення стовпця для першої тетради
    row2 = int(input2[0] + input2[3], 2)  # Визначення рядка для другої тетради
    col2 = int(input2[1:3], 2)  # Визначення стовпця для другої тетради

    output1 = format(S_BOX[row1][col1], '04b')  # Вихідна перша тетрада
    output2 = format(S_BOX[row2][col2], '04b')  # Вихідна друга тетрада

    return output1 + output2  # Повертаємо об'єднані результати обробки обох тетрад

# Функція для зворотного S-блоку
def reverse_s_box(input_bits):
    output = ""
    for bit in input_bits:
        index = S_BOX[int(bit, 2)].index(int(bit, 2))
        output += format(index, '04b')
    return output

if __name__ == "__main__":
    input_data = "00101010"
    s_result = s_box(input_data)
    print("S-блок прямого перетворення:", s_result)
    reverse_s_result = reverse_s_box(s_result)
    print("S-блок зворотного перетворення:", reverse_s_result)
