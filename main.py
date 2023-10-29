def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    user_input = input()
    # Step 2: Split the input string into a list of strings based on commas
    input_list = user_input.split(",")
    # Step 3: Convert the list of strings to a list of floats
    float_list = [float(item) for item in input_list]
    return float_list
def calc_average_temperature(num_list):
    average = sum(num_list)/ len(num_list)
    return average
def find_min_max(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    return min_temp, max_temp
def sort_temperature(num_list):
    num_list.sort()  # This will sort num_list in-place in ascending order
    return num_list
def calc_median_temperature(num_list):
    n = len(num_list)

    if n % 2 == 1:
        # If the number of elements is odd, return the middle value as the median
        median = num_list[n // 2]
    else:
        # If the number of elements is even, calculate the average of the two middle values
        middle1 = num_list[(n // 2) - 1]
        middle2 = num_list[n // 2]
        median = (middle1 + middle2) / 2
    return median
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Number List: ", num_list)
    print("Average Number: ", calc_average_temperature())
    print("Minimum & Maximum: ", find_min_max())
    print("Sorted List: ", sort_temperature())
    print("Median: ", calc_median_temperature())

    if __name__ == "__main__":
        main()
