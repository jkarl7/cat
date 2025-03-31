import sys
import magic
import getopt

text_files = []

supported_file_formats = ["text/plain", "inode/x-empty"]

options = "n:h:"

partial_text_lines = 0


def validate_program_args(arguments):
    for opt, arg in arguments:
        if opt in "-n":
            try:
                global partial_text_lines
                partial_text_lines = int(arg)
            except:
                print("-n option argument must be integer")
                exit(0)
    return True


def validate_file_args(file_names):
    if len(file_names) == 0:
        print('Provide text files to be printed out')
        exit(0)

    for file in file_names:
        file_type = magic.from_file(file, mime=True)
        if file_type not in supported_file_formats:
            print('File: ' + file + ' not supported. Use --help to get list of supported fileformats')
            exit(0)
        print(file_type)


def print_partial_contents_to_stdout(values, nr_of_lines):
    for filename in values:
        with open(filename) as file:
            head = [next(file) for _ in range(partial_text_lines)]
        print(head)


def print_contents_to_stdout(arguments, values):
    for opt, arg in arguments:
        if opt in "-n":
            print_partial_contents_to_stdout(values, arg)
            exit(0)

    for filename in values:
        with open(filename) as file:
            while line := file.readline():
                print(line.rstrip())


if __name__ == '__main__':
    arguments, values = getopt.getopt(sys.argv[1:], options)
    print(arguments)
    validated_program_args = validate_program_args(arguments)
    validate_file_args(values)
    print_contents_to_stdout(arguments, values)
