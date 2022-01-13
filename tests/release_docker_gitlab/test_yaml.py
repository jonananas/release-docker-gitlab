import yaml
from ruamel.yaml import YAML


def skip_test_yaml_read():
    with open("/Users/jonas/projects/demonstrator/.gitlab-ci.yml") as file:
        gitlab_ci = yaml.load(file)
    assert gitlab_ci['variables']['DOCKER_IMAGE_TAG'] == "${CI_COMMIT_REF_SLUG}-${CI_COMMIT_SHORT_SHA}"


def skip_test_that_yaml_writes():
    with open("/Users/jonas/projects/demonstrator/.gitlab-ci.yml") as file:
        gitlab_ci = yaml.load(file)
    gitlab_ci['variables']['DOCKER_IMAGE_TAG'] = "0.0.1"

    with open(r'./yaml-result.yml', 'w') as file:
        yaml.dump(gitlab_ci, file)


# Below settings makes only the required setting change
# diff ../demonstrator/.gitlab-ci.yml ruamel_yaml-result.yml
def skip_test_that_ruamel_yaml_writes():
    yaml = YAML()
    yaml.default_flow_style = False
#    yaml.explicit_start = True
    yaml.indent(mapping=2, offset=2)
    yaml.preserve_quotes = True
    yaml.width = 512
    with open("/Users/jonas/projects/demonstrator/.gitlab-ci.yml") as file:
        gitlab_ci = yaml.load(file)
    gitlab_ci['variables']['DOCKER_IMAGE_TAG'] = "0.0.1"

    with open(r'./ruamel_yaml-result.yml', 'w') as file:
        yaml.dump(gitlab_ci, file)
