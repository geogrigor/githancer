from setuptools import setup, find_packages

setup(
    name='githancer',
    version='0.1.0',
    url='https://github.com/geogrigor/githancer',
    author='Geo Grigor',
    author_email='geogrigor@gmail.com',
    description='Simple git productivity tool',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'githancer = githancer.githancer:main',
        ],
    },
)