from setuptools import find_packages, setup

from aquainfo import VERSION


def read_requirements(filename="requirements.txt"):
    return [ line.strip() for line in open(filename) if line.strip() and line[0].strip() != '#' ]



setup(
    name='django-aquarium-info',
    version=VERSION,
    author='Dave Gabrielson',
    author_email='Dave.Gabrielson@Gmail.Com',
    description='An aquarium information database',
    url="",
    license="",
    packages=find_packages(exclude=['aquainfo.demo_site']),
    install_requires=read_requirements(),
    zip_safe=False,
    include_package_data=True,
)
