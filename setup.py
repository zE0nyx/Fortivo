from setuptools import setup, find_packages

setup(
    name='fortivo',
    version='1.0.0',
    description='A tool to evaluate password strength based on length, complexity, and entropy.',
    author='Arghya Bala',
    author_email='arghyabalaofficial0473@gmail.com',
    url='https://github.com/zE0nyx/fortivo',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fortivo=fortivo:password_check',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
