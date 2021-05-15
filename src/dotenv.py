from fileio import FileIO


class DotEnv:
    def __init__(self):
        self.fileio: FileIO = FileIO()

    def read(self, filename: str) -> dict:
        res = dict()
        for line in self.fileio.readlines(filename):
            key, value = line.split("=")
            res[key] = value[:-1]
        return res

    def write(self, filename: str, envdict):
        lines = list()
        for key, value in envdict.items():
            lines.append(f"{key}={value}\n")
        self.fileio.writelines(filename, lines)
