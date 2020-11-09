from setuptools import setup, find_packages
import calendar
import time

# Set packages
packages = find_packages()

# Set requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Set build number
ts = calendar.timegm(time.gmtime())

setup(
    name='microfaune_ai',
    version='1.0.1' + ts.__str__(),
    author="Microfaune - Data For Good",
    author_email="microfaune@fake.com",
    url='https://github.com/microfaune/microfaune_ai',
    download_url='https://github.com/microfaune/microfaune_ai/tree/main',
    description='Module package used for the Microfaune project',
    long_description='Biodiversity evaluation and monitoring is the first step toward its protection. The goal of the Microfaune project is to evaluate avifauna in Cité Internationale park (Paris, France) from audio recordings',
    license='Open license',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: Free For Educational Use',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Multimedia :: Sound/Audio :: Analysis'
    ],
    install_requires=requirements,
    packages=packages,
    package_data={'': ['data/*.h5']}
)
