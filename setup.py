# https://awaywithideas.com/the-optimal-python-project-structure/

# https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
# https://testdriven.io/blog/modern-tdd/
# https://alex.dzyoba.com/blog/python-import/

# http://automatetheboringstuff.com/#toc

# Check out my article on python anaconda 

import setuptools

#setuptools.setup(name='mcdeltaxp', packages=['mcdeltaxp'])

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='my_project',
                 packages=['my_project'],
                 install_requires=install_requires)