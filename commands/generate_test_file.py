import os

def main():
    # Step 1: Prompt user for directory
    directory = '/workspaces/python/'
    directory += input("Please enter a directory path (e.g., loops/labs): ")
    
    # Step 2: Append a '/' at the end if missing
    if not directory.endswith('/'):
        directory += '/'
    
    # Step 3: Get the root name (last directory)
    root = os.path.basename(os.path.dirname(directory))
    
    # Create the directory if it doesn't exist
    # if not os.path.exists(directory):
    #     os.makedirs(directory)
    
    # Step 4: Create a file called <root>.py
    # with open(f"{directory}{root}.py", 'w') as f:
    #     f.write("")
    
    # Step 5: Create three input files
    # for i in range(1, 4):
    #     with open(f"{directory}input0{i}.txt", 'w') as f:
    #         f.write("")

    # Step 6: Create three test files
    # for i in range(1, 4):
    #     with open(f"{directory}test0{i}.txt", 'w') as f:
    #         f.write("")            
    
    # Step 7: Create test_<root>.py with the specified code
    test_code = '''
class TestInput:
        
    def test_input_from_user(self):

        with open("actual.txt") as actual_output:
            actual = ''
            for line in actual_output:
                actual += line.strip() + '\\n'

        with open("expected.txt") as expected_output:
            expected = ''
            for line in expected_output:
                expected += line.strip() + '\\n'

        assert actual.strip() == expected.strip()            
'''
    
    with open(f"{directory}test_{root}.py", 'w') as f:
        f.write(test_code.strip())
    
    # Create empty actual.txt and expected.txt files for testing
    # with open(f"{directory}actual.txt", 'w') as f:
    #     f.write("")
    
    # with open(f"{directory}expected.txt", 'w') as f:
    #     f.write("")
    
    print(f"\nSetup completed successfully!")
    # print(f"Root directory name: {root}")
    # print(f"Created files:")
    # print(f"  - {root}.py")
    # print(f"  - input01.txt, input02.txt, input03.txt")
    print(f"  - test_{root}.py")

if __name__ == "__main__":
    main()