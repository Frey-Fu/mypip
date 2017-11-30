import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'mypip.py')
version_line = [line for line in open(module_path)
                        if line.startswith('__version__')][0]


setuptools.setup(
    name="mypip",
    version='0.1',
    description="mypip",
    url="https://git.myserver.com/foobar-utils/",

    author="Wei Fu",
    author_email="fuwei@bmqb.com",

    long_description=open('README.rst').read(),

    zip_safe=False,

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
