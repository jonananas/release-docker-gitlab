
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


# Doing
- Trying to make pytest find tests and modules automatically, ie not by manipulating PYTHONPATH
    - Created src + tests structure - no success
    - Added __init__.py to src - no success
    - Created setup.py, and doing ´python3 setup.py develop´ - might work, but current nameclash with module semver.
        - How namespace?
        - `python3 setup.py develop --uninstall` to remove link(?)

This link suggests doing pip install -e instead of ´python3 setup.py develop´
https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install
