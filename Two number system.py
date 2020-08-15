#Exercise number one.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def pairs(numbers, k):
    for i in range(len(numbers)):
        for a in range(i + 1, len(numbers)):
            if numbers[i] + numbers[a] == k:
                return True
    return False

# I have allowed it to take k from the question from the user. 

check_num = int(input("Enter the number you want to check:\n "))

print(pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], check_num))
