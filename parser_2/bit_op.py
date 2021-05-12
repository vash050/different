# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

# first_num = 5
# second_num = 6
# left_two = first_num << 2
# right_two = first_num >> 2
# res_bit_and = first_num & second_num
# res_bit_or = first_num | second_num
# res_bit_xor = first_num ^ second_num
# print(bin(first_num))
# print(bin(second_num))
# print(res_bit_and, bin(res_bit_and))
# print(res_bit_or, bin(res_bit_or))
# print(res_bit_xor, bin(res_bit_xor))
# print(left_two, bin(left_two))
# print(right_two, bin(right_two))

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

while True:
    try:
        first_letter = (input("")).lower()
        second_letter = (input("")).lower()
        print(alphabet.index(first_letter) + 1)
        print(alphabet.index(second_letter) + 1)
        print(len(alphabet[alphabet.index(first_letter):alphabet.index(second_letter) - 1]))
        break
    except Exception as e:
        print(e)
        continue

