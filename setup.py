import setuptools

with open("readme.md","r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.1"

REPO_NAME = "Facebook Post Status Prediction"
AUTHOR_USER_NAME = "vinayaka.uppar"
SCR_REPO = "facebookpostpredict"
AUTHOR_EMAIL ="vinayakavirat008@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_eamil=AUTHOR_EMAIL,
    description="A small python package for facebook app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"source"},
    packages=setuptools.find_packages(where="source")
)
    