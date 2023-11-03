from setuptools import find_packages, setup
from typing import List

    
# def get_requirements(file_path: str) -> List[str]:
#     '''
#     this returns a string
#     '''

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str):
    '''
    this returns the list of all the requirements
    '''
    with open(file_path) as f_obj:
        requirements = [r.replace("/n","") for r in f_obj.readlines()]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Dipan",
    author_email="dipanbanik104@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)