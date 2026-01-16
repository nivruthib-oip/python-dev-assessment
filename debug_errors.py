def calculate_average(numbers):
   
    try:
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)
    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list.")
        return None


def get_list_element(my_list, index):
    
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index is out of bounds.")
        return None
    except TypeError:
        print("Error: Provided input is not a list.")
        return None


# Example data
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  

# Testing calculate_average
print("Average of data1:", calculate_average(data1))
print("Average of data2:", calculate_average(data2))
print("Average of data3:", calculate_average(data3))

print("\nTesting get_list_element")

# Valid access
print(get_list_element([1, 2, 3], 1))

# Out-of-bounds index
print(get_list_element([1, 2, 3], 5))

# Incorrect type
print(get_list_element("not a list", 2))
