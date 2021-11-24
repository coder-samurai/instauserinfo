from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Get Instagram user info'


# Setting up

setup(
    name="instauserinfo",
    version=VERSION,
    author="SamuraiCoder",
    author_email="<aelboutaheri@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'instagram', 'requests'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)