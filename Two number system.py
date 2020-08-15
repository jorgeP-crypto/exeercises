def pairs(numbers, k):
    for i in range(len(numbers)):
        for a in range(i + 1, len(numbers)):
            if numbers[i] + numbers[a] == k:
                return True
    return False


check_num = int(input("Enter the number you want to check:\n "))

print(pairs([2, 5, 1, 6, 8, 10], check_num))
