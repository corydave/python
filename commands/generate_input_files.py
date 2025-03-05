def generate_input_files():
    number_of_test_cases = int(input('How many test cases? '))

    command = ''
    file_number = ''

    for number in range(number_of_test_cases):

        file_number = ''

        if number < 10:
            file_number = '0' + str(number+1)

        command += f'touch input{file_number}.txt'

        if number < number_of_test_cases - 1:
            command += ' && '

    print(command)

if __name__ == "__main__":
    generate_input_files()