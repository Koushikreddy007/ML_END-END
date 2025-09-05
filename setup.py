from setuptools import find_packages,setup
from typing import List

dot='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if dot in requirements:
            requirements.remove(dot)

setup(
    name='mlproject',
    version='0.0.1',
    author='Koushik',
    author_email='koushikreddy92@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)