from setuptools import find_packages , setup
from typing import List

hyphen_e = '-e .'

def get_req(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)        
        return requirements


setup(
    name = 'DiamondPricePredicrion',
    version = '0.0.1',
    author = 'Aniket',
    author_email = "kittuaniket2003@gmail.com",
    install_requires = get_req('req.txt'),
    packages = find_packages()
)