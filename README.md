
# Release Docker GitLab

```bash
python3 -m release_docker_gitlab
```

Release a GitLab Docker project, ie
- From a branch with 
    - DOCKER_IMAGE_TAG=x.y.z-SNAPSHOT in .env
    - LAST_IMAGE_TAG=x.y.z in .env
    - DOCKER_IMAGE_TAG=<any string> in .gitlab-ci.yml
- Create a git tag x.y.z with
    - DOCKER_IMAGE_TAG=x.y.z in .env
    - LAST_IMAGE_TAG=x.y.z in .env
    - DOCKER_IMAGE_TAG=x.y.z in .gitlab-ci.yml
- Create a following commit with
    - DOCKER_IMAGE_TAG=x.y.(z+1)-SNAPSHOT in .env
    - LAST_IMAGE_TAG=x.y.z in .env
    - DOCKER_IMAGE_TAG=<any string>

You can also do
```bash
python3 -m release_docker_gitlab --help
```

## Installing

Not available as whl yet, you need to 

```bash
pip3 install -e .
```

after cloning.

## Testing

```bash
pytest
```

## Example

To run the example, do
```bash
cp -r example-project-root ..
cd ../example-project-root
git init .
python3 -m release_docker_gitlab

## TODO
- Check https://www.freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2/ to distribute via github.
- How make release.sh installed as a command-line tool?
