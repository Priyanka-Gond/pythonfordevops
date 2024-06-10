def input_numbers():
    numbers = []
    while True:
        user_input = input("Enter an integer (or type 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return numbers

# Calling the function and printing the resulting list
numbers_list = input_numbers()
print("The list of numbers you entered:", numbers_list)
l=len(numbers_list)
for i in range(l):
    for j in range(l):
        if numbers_list[i] < numbers_list[j]:
            temp=numbers_list[i]
            numbers_list[i]=numbers_list[j]
            numbers_list[j]=temp
print(numbers_list[0])
print(numbers_list[1])