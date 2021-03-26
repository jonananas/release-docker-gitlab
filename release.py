from dotenv import DotEnv
from  ruamel.yaml import YAML
"""
1. Get current ver from .env
2. Propose release-ver and next-snapshot - semver-match
3. Update .env to release-ver
4. Update .gitlab-ci to release-ver
5. git commit
6. update to next-snapshot
7. git commit


NEWTAG=$1
NEXTTAG=$2
echo Releasing $NEWTAG, $NEXTTAG-SNAPSHOT is next
perl -i -pe"s/DOCKER_IMAGE_TAG=[^-]*-SNAPSHOT/DOCKER_IMAGE_TAG=$NEWTAG/g" .env || exit -1
git commit -m "Release $NEWTAG" .env || exit -1
git tag $NEWTAG || exit -1
perl -i -pe"s/DOCKER_IMAGE_TAG=[^\s]*/DOCKER_IMAGE_TAG=$NEXTTAG-SNAPSHOT/g" .env || exit -1
git commit -m "Next snapshot version $NEXTTAG-SNAPSHOT" .env || exit -1
echo To publish, do:
echo git push
echo git push origin $NEWTAG
"""

class SemVer:
    None

def set_env_ver(ver: SemVer, filename=".env"):
    dotenv = DotEnv()
    envdict = dotenv.read(filename)
    envdict['DOCKER_IMAGE_TAG'] = ver
    dotenv.write(".env", envdict)

def get_env_ver(filename=".env"):
    dotenv = DotEnv()
    envdict = dotenv.read(filename)
    return envdict['DOCKER_IMAGE_TAG']

def set_gitlabci_ver(ver: SemVer, filename = ".gitlab-ci.yml"):
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

def get_gitlabci_ver():
    yaml = YAML()
    with open("/Users/jonas/projects/demonstrator/.gitlab-ci.yml") as file:
        gitlab_ci = yaml.load(file)
    return gitlab_ci['variables']['DOCKER_IMAGE_TAG']

def lets_go():
