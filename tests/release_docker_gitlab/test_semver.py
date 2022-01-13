from pytest import raises
from release_docker_gitlab.semver import SemVer


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
    assert semver.extra is None


def test_that_fails_without_major_minor_patch():
    with raises(Exception):
        SemVer("0.1")


def test_str():
    assert str(SemVer("0.1.2-SNAPSHOT")) == SemVer("0.1.2-SNAPSHOT").str()
    assert SemVer("0.1.2-SNAPSHOT").str() == "0.1.2-SNAPSHOT"
    assert SemVer("0.1.2").str() == "0.1.2"
    assert SemVer("0.1.2-").str() == "0.1.2-"


def test_next_patch_of_snapshot():
    assert SemVer("0.1.2-SNAPSHOT").next_patch() == SemVer("0.1.3-SNAPSHOT")


def test_release():
    semver = SemVer("0.1.2-SNAPSHOT")
    assert semver.release().str() == "0.1.2"


def test_equality():
    verstr = "0.1.2-SNAPSHOT"
    semver = SemVer(verstr)
    same = SemVer("0.1.2-SNAPSHOT")
    other = SemVer("0.1.2")
    assert semver == same
    assert semver != other
    assert semver != verstr
    assert semver is not None
