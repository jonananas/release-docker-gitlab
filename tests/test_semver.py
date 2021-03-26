from pytest import raises
from semver import SemVer

def test_has_major_minor_patch():
    semver = SemVer("0.1.2-SNAPSHOT")
    assert semver.major == 0
    assert semver.minor == 1
    assert semver.patch == 2
    assert semver.extra == "-SNAPSHOT"

def test_that_extra_is_none():
    semver = SemVer("0.1.2")
    assert semver.major == 0
    assert semver.minor == 1
    assert semver.patch == 2
    assert semver.extra == None

def test_that_fails_without_major_minor_patch():
    with raises(Exception):
        SemVer("0.1")

def test_str():
    assert SemVer("0.1.2-SNAPSHOT").__str__() == "0.1.2-SNAPSHOT"
    assert SemVer("0.1.2").__str__() == "0.1.2"
    assert SemVer("0.1.2-").__str__() == "0.1.2-"

def test_next_patch_of_snapshot():
    assert SemVer("0.1.2-SNAPSHOT").next_patch().__str__() == SemVer("0.1.3-SNAPSHOT").__str__()

def test_release():
    semver = SemVer("0.1.2-SNAPSHOT")
    assert semver.release().__str__() == "0.1.2"
