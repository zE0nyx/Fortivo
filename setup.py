from setuptools import setup, find_packages

setup(
    name='fortivo',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fortivo=fortivo:main',
        ],
    },
    install_requires=[
        # None for now
    ],
    description='This tool evaluates the password strength based on length, complexity, and entropy.',
    long_description=open('README.md').read(),  # Read from a README file
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/zE0nyx',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6'
    ],
    python_requires='>=3.6',
)
