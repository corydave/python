import os


def generate_expected_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    files = os.listdir(dir_path)
    python_program_name = input("Program name? ")

    command = ''

    for file in files:
        # print(file)
        file_name_raw = file.split('.')
        # print('===== '+ file_name[0])

        file_name = file_name_raw[0]
        print(file_name[:5])

        if file_name[:5] == 'input' and 'generation' not in file:
            command += f'python3 {python_program_name} < {file} > expected{file[5:7]}.txt && '



    print(command[0:len(command)-3])


  

if __name__ == "__main__":
    generate_expected_files()