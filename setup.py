from setuptools import setup, find_packages

setup(
    name='anity',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'anity = anity.anity:cli',
        ],
    },
)
