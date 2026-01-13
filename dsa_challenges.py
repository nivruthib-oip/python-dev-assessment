 #Function 1
def filter_and_sort_evens(numbers):
    evens = []
    
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    
    evens.sort()
    return evens
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = filter_and_sort_evens(numbers)
print(result)


# CALL FUNACTION
numbers_test = [3, 1, 4, 1, 5, 9, 2, 6]
print("Filtered and sorted evens:", filter_and_sort_evens(numbers_test))


#Function 1
def count_character_frequency(text):
    frequency = {}

    text = text.lower()

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# CALL FUNACTION

text = "NivruthiBandari"
result = count_character_frequency(text)

print("Character frequency:", result)