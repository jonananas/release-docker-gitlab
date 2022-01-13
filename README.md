
# Release Docker GitLab

## Install and run

```sh
pip3 install git+https://github.com/jonananas/release-docker-gitlab#egg=release-docker-gitlab
release_docker_gitlab
```

## What does it do?

Release a GitLab Docker project that contains current version in the project root .env file as this:

```txt
DOCKER_IMAGE_TAG=0.0.9-SNAPSHOT
LAST_IMAGE_TAG=0.0.8
```

and a .gitlab-ci.yml as this:

```yaml
variables:
  DOCKER_IMAGE_TAG: ${CI_COMMIT_REF_SLUG}-${CI_COMMIT_SHORT_SHA}
```

it will

- Assert that current branch is either `master`, `main`, or `release/...`
- Propose next release tag x.y.z
- Create a git commit with updated
    - DOCKER_IMAGE_TAG=x.y.z in .env
    - LAST_IMAGE_TAG=x.y.z in .env
    - DOCKER_IMAGE_TAG=x.y.z in .gitlab-ci.yml
- Create git tag x.y.z
- Create a another commit with
    - DOCKER_IMAGE_TAG=x.y.(z+1)-SNAPSHOT in .env
    - LAST_IMAGE_TAG=x.y.z in .env
    - DOCKER_IMAGE_TAG=<any string>


## Why SNAPSHOT?

The premise is that you have a docker project with immutable released tags, and mutable local tags ending with -SNAPSHOT.
It makes sense to build releases automatically from pushed tags, for example because your image is used as a command line tool and not as a service on the cloud. (As opposed to continous deployment master)

## Installing from repo

```sh
pip3 install git+https://github.com/jonananas/release-docker-gitlab#egg=release-docker-gitlab
```

### Installing from source

```sh
git clone https://github.com/jonananas/release-docker-gitlab
pip3 install -e release-docker-gitlab
```

## Testing

```sh
pytest
```

## Example

To run the example, do
```sh
cp -r example-project-root ..
cd ../example-project-root
git init .
release_docker_gitlab
```
