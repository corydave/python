import os


def generate_expected_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    files = os.listdir(dir_path)

    directory = '/workspaces/python/'
    directory += input('What is the path? ')

    if not directory.endswith('/'):
        directory += '/'

    python_program_name = input('What is the name of the Python program? ')
    directory += python_program_name[:-3] + '/'

    print(f'Directory = {directory}')
    print(f'File name = {python_program_name}')
    print()      

    command = ''

    for file in files:
        # print(file)
        file_name_raw = file.split('.')
        # print('===== '+ file_name[0])

        file_name = file_name_raw[0]
        print(file_name[:5])

        if file_name[:5] == 'input' and 'generation' not in file:
            command += f'python3 {directory}{python_program_name} < {directory}{file} > {directory}expected{file[5:7]}.txt && '



    print(command[0:len(command)-3])


  

if __name__ == "__main__":
    generate_expected_files()