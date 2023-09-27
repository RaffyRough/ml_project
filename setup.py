from setuptools import find_packages, setup
from typing import List

AUTORUN = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if AUTORUN in requirements:
            requirements.remove(AUTORUN)
    return requirements

setup( name = 'ds_project',
    version='0.0.1',
    author='Oce Mapp',
    author_email='oce.mapp@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')    )