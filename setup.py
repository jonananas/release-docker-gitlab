import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="release-docker-gitlab",
    version="0.0.1-SNAPSHOT",
    author="Jonas Andersson",
    author_email="jonananas@gmail.com",
    description="Release Docker GitLab projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonananas/release-docker-gitlab",
    project_urls={
        "Bug Tracker": "https://github.com/jonananas/release-docker-gitlab/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'GitPython>=3.1.14',
        'ruamel.yaml>=0.17.21'
    ],
    entry_points={
        'console_scripts': ['release-docker-gitlab=release_docker_gitlab.release:release'],
    },
    python_requires=">=3.9",
)
