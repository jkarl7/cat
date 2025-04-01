import getopt


class OptionsValidator:
    _instance = None
    options = "n:h"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def validate_program_options(self, program_input_options):
        try:
            options, values = getopt.getopt(program_input_options, self.options)
        except getopt.GetoptError as e:
            print("Error: " + e.msg)
            exit(0)

        for opt, arg in options:
            if opt in "-n":
                try:
                    int(arg)
                except:
                    print("-n option argument must be integer")
                    exit(0)
        return options, values
