from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='outagesrunner',
      version=version,
      description="Runner application for Outages",
      long_description="""\
        """,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Greg Jurman',
      author_email='gdj2214@rit.edu',
      url='https://github.com/gregjurman',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
            'boto',
            'sqlalchemy',
            'lxml',
            'BeautifulSoup'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
