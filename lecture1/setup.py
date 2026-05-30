from setuptools import find_packages,setup
from typing import List

hypen_e_dot="-e ." #to igore -e . from requirements

def get_requirements(file_path:str)->List[str]:
    '''This function will return list of requiremnts'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #considers \n as well
        requirements=[req.replace("\n","") for req in requirements]
        # requirements=requirements=[req.strip() for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(  #meta data information about project
    name="mlproject", #name
    version='0.0.1', #version can be updates when we change
    author="Dharani",
    author_email="pandukonda600@gmail.com",
    packages=find_packages(), #--> it checks how many files have "__init__.py" and considers foldername as a package and builds to import it easily
    install_requires=get_requirements('requirements.txt')
#     '''install_requires=['pandas','numpy','seaborn'],''' #installs libraries automatically
# #setup.py connects the packages(actual code) using find_packages()
)