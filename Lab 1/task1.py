def add_numbers():
    numbers = input("Enter two or more numbers separated by spaces: ")
    num_list = numbers.split()
    if len(num_list) < 2:
        print("You must enter at least two numbers")
        return
    total = 0
    for num in num_list:
        if not num.isdigit() and not num.replace(".", "").isdigit():
            print("Input must contain only numbers")
            return
        total += float(num)
    print("The sum of the numbers is:", total)

add_numbers()