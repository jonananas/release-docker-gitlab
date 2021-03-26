from re import search

class SemVer:
    
    def __init__(self, version:str):
        # From https://github.com/npm/node-semver/issues/32
        semver = ("^([0-9]+)"                     # major
                "\.([0-9]+)"                      # minor
                "\.([0-9]+)"                      # patch
#                "(-[0-9]+-?)?",                  # build
                "([a-zA-Z-+][a-zA-Z0-9-\.:]*)?$") # tag
        # Regex from https://gist.github.com/jhorsman/62eeea161a13b80e39f5249281e17c39
        m = search(semver, version)
        self.major = int(m.group(1))
        self.minor = int(m.group(2))
        self.patch = int(m.group(3))
        self.extra = m.group(4)

    def fromstring(semver:str):
        return SemVer(semver)

    def fromparts(major: int, minor:int, patch:int, extra:str = None):
        semver = SemVer("0.0.0")
        semver.major = major
        semver.minor = minor
        semver.patch = patch
        semver.extra = extra
        return semver

    def next_patch(self):
        return self.__class__.fromparts(self.major, self.minor, self.patch + 1, self.extra)

    def release(self):
        return self.__class__.fromparts(self.major, self.minor, self.patch)

    def __str__(self):
        extra = self.extra if self.extra else ""
        return f"{self.major}.{self.minor}.{self.patch}{extra}"
