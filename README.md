
# Release Docker GitLab

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
```
