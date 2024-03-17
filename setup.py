from setuptools import setup, find_packages

setup(
    name='chattyboy',
    version='1.0',
    packages=find_packages(),
 entry_points={
    'console_scripts': [
        'chattyboy=chattyboy.chatbot:main',
    ],
},)
