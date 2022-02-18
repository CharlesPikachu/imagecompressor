'''
Function:
    setup the imagecompression
Author:
    Charles
微信公众号:
    Charles的皮卡丘
GitHub:
    https://github.com/CharlesPikachu
'''
import imagecompression
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name=imagecompression.__title__,
    version=imagecompression.__version__,
    description=imagecompression.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=imagecompression.__author__,
    url=imagecompression.__url__,
    author_email=imagecompression.__email__,
    license=imagecompression.__license__,
    include_package_data=True,
    package_data={},
    install_requires=list(open('requirements.txt', 'r').readlines()),
    zip_safe=True,
    packages=find_packages(),
)