def find_pairs (n):
    result = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if pair_sum != 0 and n % pair_sum == 0:
                result_append(f"({1} + {j})")
                return ','.join(result)
            n = int(input("Введите число n (от 3 до 20): "))
            if 3 <= n <= 20:
                password = find_pairs (n)
                print("найденные пары", password )
            else:
                print("Число должно быть в диапазоне от 3 до 20.")