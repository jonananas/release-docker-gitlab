from dotenv import DotEnv
from ruamel.yaml import YAML
from semver import SemVer
from git import Repo


def set_env_ver(ver: SemVer, filename=".env"):
    dotenv = DotEnv()
    envdict = dotenv.read(filename)
    envdict['DOCKER_IMAGE_TAG'] = ver
    dotenv.write(".env", envdict)


def get_env_ver(filename=".env") -> SemVer:
    dotenv = DotEnv()
    envdict = dotenv.read(filename)
    return SemVer(envdict['DOCKER_IMAGE_TAG'])


def set_env_latest(ver: SemVer, filename=".env"):
    dotenv = DotEnv()
    envdict = dotenv.read(filename)
    envdict['LATEST_RELEASE'] = ver
    dotenv.write(".env", envdict)


def has_env_latest(filename=".env") -> bool:
    dotenv = DotEnv()
    envdict = dotenv.read(filename)
    return 'LATEST_RELEASE' in envdict


def get_yaml_preserve_config():
    # Settings to preserve a typical .gitlab-ci.yml file as it was
    yaml = YAML()
    yaml.default_flow_style = False
    yaml.indent(mapping=2, offset=2)
    yaml.preserve_quotes = True
    yaml.width = 512
    return yaml


def set_gitlabci_ver(ver: str, filename=".gitlab-ci.yml"):
    yaml = get_yaml_preserve_config()
    with open(filename) as file:
        gitlab_ci = yaml.load(file)
    gitlab_ci['variables']['DOCKER_IMAGE_TAG'] = ver

    with open(filename, 'w') as file:
        yaml.dump(gitlab_ci, file)


def get_gitlabci_tag(filename=".gitlab-ci.yml") -> str:
    yaml = YAML()
    with open(filename) as file:
        gitlab_ci = yaml.load(file)
    return gitlab_ci['variables']['DOCKER_IMAGE_TAG']


def git_commit(commit_message: str):
    git = Repo()
    # print("git commit -m " + commit_message)
    git.index.add([".env", ".gitlab-ci.yml"])
    git.index.commit(commit_message)


def git_tag(tag: str):
    git = Repo()
    git.create_tag(tag)


def enforce_snapshot_version(curr_ver):
    if curr_ver.extra != "-SNAPSHOT":
        raise Exception(f"Release only allowed on snapshot versions, current version is {curr_ver}.")


def enforce_master_branch_or_release_branch():
    git = Repo()
    if str(git.active_branch) != "master" and not str(git.active_branch).startswith("release/"):
        raise Exception(f"Release only allowed from master or release/<ver>, current branch is {git.active_branch}.")


def release():
    # Add check that
    # - nothing uncommitted?
    enforce_master_branch_or_release_branch()
    curr_ver = get_env_ver()
    enforce_snapshot_version(curr_ver)
    ci_tag = get_gitlabci_tag()
    next_ver = curr_ver.next_patch()
    if ci_tag.startswith(str(curr_ver)):
        ci_tag = ci_tag.replace(str(curr_ver), str(next_ver))
    release_ver = curr_ver.release()
    print(f"Releasing {release_ver} with nextver {next_ver}, next ci-tag {ci_tag}, ok?")
    input(f"Continue? Any/Ctrl-Break")

    set_env_ver(release_ver)
    if has_env_latest():
        set_env_latest(release_ver)
    set_gitlabci_ver(release_ver.str())
    git_commit(f"Release {release_ver}")
    git_tag(release_ver.str())

    set_env_ver(next_ver)
    set_gitlabci_ver(ci_tag)
    git_commit(f"Next snapshot version {next_ver}")


release()
