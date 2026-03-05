#!/usr/bin/env python3

import os
import shutil
from pathlib import Path
from setuptools.command.install import install
from distutils.command.clean import clean
from setuptools import setup, find_packages


BLUESCAN_PATH = os.path.abspath(Path(__file__).parent)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class MyInstall(install):
    def run(self):
        super().run()
        print('[INFO] install bluing_prompt.bash')
        shutil.copy(
            'src/bluing/bluing_prompt.bash', '/etc/bash_completion.d'
        )


class MyClean(clean):
    def run(self):
        super().run()
        dirs = [
            os.path.join(BLUESCAN_PATH, 'build'),
            os.path.join(BLUESCAN_PATH, 'dist'),
            os.path.join(BLUESCAN_PATH, 'src', 'bluing.egg-info'),
            os.path.join(BLUESCAN_PATH, 'src', 'bluing', '__pycache__')
        ]

        for d in dirs:
            shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    setup(
        name='bluing',
        version='0.1.0',
        license = "GPLv3",
        packages=find_packages('src'), # include all packages under src
        package_dir={'':'src'}, # tell distutils packages are under src
        entry_points={
            'console_scripts': [
                'bluing=bluing.__main__:main'
            ]
        },
        package_data={
            "bluing": ["res/*.txt"]
        },
        #scripts=['src/bluing/bluing.py'],

        install_requires=[
            'pybluez>=0.23', 'bluepy>=1.3.0', 'docopt>=0.6.2', 
            'termcolor>=1.1.0',
        ],

        # metadata to display on PyPI
        author="cyberxml",
        author_email="cyberxml#mail.com",
        description='Refactor of bluing',
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        url='https://github.com/cyberxml/bluing',
        # project_urls={
        #     "Bug Tracker": "None",
        #     "Documentation": "None",
        #     "Source Code": "None",
        # },

        cmdclass={
            'install': MyInstall,
            'clean': MyClean
        }
    )
