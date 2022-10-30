def main():
    print("ET0735 (DevOps for AIoT - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))


def display_main_menu():
    print("Enter some numbers separated by commas (e.g 18,06,28,01)")


def get_user_input():
    user_input = input()
    user_input_split = user_input.split(",")
    return [float(x) for x in user_input_split]


def calc_average_temperature(x):
    total = 0
    for numbers in x:
        total += numbers
    average = total / len(x)
    return f'The calculated average value of all temperature readings is {average}.'


def calc_min_max_temperature(x):
    maximum = max(x)
    minimum = min(x)
    print("The minimum and maximum temperature in the list is ");
    return [int(minimum), int(maximum)]


if __name__ == "__main__":
    main()
