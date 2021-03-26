from fileio import FileIO
from dotenv import DotEnv

snapshot_contents = """PUBLIC_HOSTNAME=localhost
DOCKER_IMAGE_TAG=0.0.2-SNAPSHOT
""".splitlines(keepends=True)

version_contents = """PUBLIC_HOSTNAME=localhost
DOCKER_IMAGE_TAG=0.0.3
""".splitlines(keepends=True)


# "pip install pytest-mock" required!
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args

class TestDotEnv:

    def setup(self):
        self.sut = DotEnv()
        self.NEWTAG = "0.0.3"

    def test_that_returns_dict(self, mocker):
        fileio_mock = self.mock_fileio_return(snapshot_contents, mocker)

        envdict = self.sut.read(".env")
        assert envdict['DOCKER_IMAGE_TAG'] == "0.0.2-SNAPSHOT"

    def test_that_writes_dict(self, mocker):
        fileio_mock = self.mock_fileio_return(snapshot_contents, mocker)

        envdict = self.sut.read(".env")
        envdict['DOCKER_IMAGE_TAG'] = "0.0.3"
        self.sut.write(".env", envdict)

        written = fileio_mock.writelines.call_args.args[1]
        assert written == version_contents

    def mock_fileio_return(self, contents, mocker):
        fileio_mock: FileIO = mocker.Mock()
        DotEnv.fileio = fileio_mock
        fileio_mock.readlines.return_value = contents
        return fileio_mock
