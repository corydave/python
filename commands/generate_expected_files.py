import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

files = os.listdir(dir_path)
# print(files)

python_program_name = input('What is the name of the Python program? ')

command = ''

for file in files:
    # print(file)
    file_name, file_ext = file.split('.')
    # print(file_name[:3])
    if file_name[:5] == 'input' and 'generation' not in file:
        # print(file)
        # print(file[5:])
        command += f'python3 {python_program_name} < {file} > expected{file[5:7]}.txt && '

    # print(file_name)

print(command)
# def generate_expected_files():

#     print(command)    

# if __name__ == "__main__":
#     generate_expected_files()