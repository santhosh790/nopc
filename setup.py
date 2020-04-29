'''
Setup file for nopc
'''

import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



params = dict(name="nopc",
              version="0.0.6",
              author="Santhoshkumar S",
              author_email="santhoshramuk@gmail.com",
              description="nopc: Neighborhood Opinion Centrality",
              long_description=read('README.md'),
              license="MIT",
              keywords="centrality, opinion dynamics, machine learning, statistics, influence finder, social networks, graph",
              url="https://github.com/santhosh790/nopc",
              packages=setuptools.find_packages(),
              classifiers=["Development Status :: 3 - Alpha",
                           "Intended Audience :: Developers",
                           "Intended Audience :: Science/Research",
                           "License :: OSI Approved :: MIT License",
                           "Topic :: Scientific/Engineering",
                           'Programming Language :: Python',
                           'Programming Language :: Python :: 3.5',
                           'Programming Language :: Python :: 3.6',
                           ],
              )

try:
    from setuptools import setup

    params["install_requires"] = ["numpy>=1.6.1",
                                  "scipy>=0.9.0",
                                  ]
    #params["extras_require"] = {"examples": ["parsimony>=0.2.1", "matplotlib>=1.1.1rc"],
    #                           "test": ["doctest"],
    #                           "tests": ["doctest", "nose", "unittest"],
    #                            }
except:
    from distutils.core import setup

setup(**params)