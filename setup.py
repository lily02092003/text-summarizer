from setuptools import find_packages,setup

def get_requirements(file_path:str)->List[str]:
    #return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
    if '-e.' in requirements:
        requirements.remove('-e.')
    return requirements
setup(
    name='text-summarizer',
    version='0.0.0',
    author='Srija',
    author_email='srijachakraborty123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description="NLP APP"
)