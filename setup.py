from setuptools import setup, find_packages

DESCRIPTION = 'Console controller for Shakes & Fidget Bot'
with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="mfbot-controller", 
        version='0.0.1',
        author="QueIvan",
        author_email="szewczykjan2@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['argparse'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License",
            "Operating System :: OS Independant"
        ],
        include_package_data=True,
        package_data = { "": [
            "locale/*/*/*.mo",
            "data/*.json",
            "data/*.txt",
            "data/*.tar",
            "scripts/*.py"
        ]}
)