import sys
import magic

text_files = []

supported_file_formats = ["text/plain", "inode/x-empty"]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def validate_program_args(program_args):
    if len(program_args) == 1:
        print('Provide text files to be printed out')
        exit(0)
    args = program_args[1:]

    for arg in args:
        file_type = magic.from_file(arg, mime=True)
        if file_type not in supported_file_formats:
            print('File: ' + arg + ' not supported. Use --help to get list of supported fileformats')
            exit(0)
        print(file_type)
    return program_args


def print_contents_to_stdout(args):
    for filename in args:
        with open(filename) as file:
            while line := file.readline():
                print(line.rstrip())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    validated_program_args = validate_program_args(sys.argv)
    print_contents_to_stdout(validated_program_args)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
