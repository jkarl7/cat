import sys

from validator.file_args_validator import FileArgsValidator
from validator.options_validator import OptionsValidator

partial_text_lines = 0


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
    options, values = OptionsValidator().validate_program_options(sys.argv[1:])
    FileArgsValidator().validate_program_args(values)
    print(options)
    print(values)
#   validated_program_args = validate_program_args(arguments)
#  validate_file_args(values)
#  print_contents_to_stdout(arguments, values)
