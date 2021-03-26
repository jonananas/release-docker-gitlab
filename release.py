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

def set_gitlabci_ver(ver: str, filename = ".gitlab-ci.yml"):
    yaml = YAML()
    # Settings to preserve yaml file format when writing
    yaml.default_flow_style = False
    yaml.indent(mapping=2, offset=2)
    yaml.preserve_quotes = True
    yaml.width = 512
    with open(filename) as file:
        gitlab_ci = yaml.load(file)
    gitlab_ci['variables']['DOCKER_IMAGE_TAG'] = ver
    
    with open(filename, 'w') as file:
        yaml.dump(gitlab_ci, file)

def get_gitlabci_ver(filename = ".gitlab-ci.yml") -> str:
    yaml = YAML()
    with open(filename) as file:
        gitlab_ci = yaml.load(file)
    return gitlab_ci['variables']['DOCKER_IMAGE_TAG']

def git_commit(commit_message):
    repo = Repo()
    #print("git commit -m " + commit_message)
    repo.index.add([".env", ".gitlab-ci.yml"])
    repo.index.commit(commit_message)

def release():
    curr_ver = get_env_ver()
    ci_pattern = get_gitlabci_ver()
    next_ver = curr_ver.next_patch()
    release_ver = curr_ver.release()
    input(f"Releasing {release_ver} with nextver {next_ver}, next .gitlab-ci {ci_pattern}, ok?")

    set_env_ver(release_ver)
    set_gitlabci_ver(release_ver.__str__())
    git_commit(f"Release {release_ver}")
    set_env_ver(next_ver)
    set_gitlabci_ver(ci_pattern)
    git_commit(f"Next snapshot version {next_ver}")

release()
