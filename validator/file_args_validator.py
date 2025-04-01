from magic import magic


class FileArgsValidator:
    _instance = None
    supported_file_formats = ["text/plain", "inode/x-empty"]

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def validate_program_args(self, arguments):
        if len(arguments) == 0:
            print('Provide text files to be printed out')
            exit(0)

        for file in arguments:
            try:
                file_type = magic.from_file(file, mime=True)
            except FileNotFoundError as e:
                print(e.strerror + ". File: " + e.filename)
                exit(0)
            if file_type not in self.supported_file_formats:
                print('File: ' + file + ' not supported. Use --help to get list of supported fileformats')
                exit(0)
            print(file_type)
