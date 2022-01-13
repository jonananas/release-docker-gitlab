from typing import List


class FileIO:
    def readlines(self, filename: str) -> List[str]:
        with open(filename, "r") as file:
            return file.readlines()

    def writelines(self, filename: str, lines: List[str]):
        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
