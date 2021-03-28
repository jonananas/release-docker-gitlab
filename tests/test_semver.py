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
    assert str(SemVer("0.1.2-SNAPSHOT")) == "0.1.2-SNAPSHOT"
    assert str(SemVer("0.1.2")) == "0.1.2"
    assert str(SemVer("0.1.2-")) == "0.1.2-"

def test_next_patch_of_snapshot():
    assert str(SemVer("0.1.2-SNAPSHOT").next_patch()) == str(SemVer("0.1.3-SNAPSHOT"))

def test_release():
    semver = SemVer("0.1.2-SNAPSHOT")
    assert str(semver.release()) == "0.1.2"
