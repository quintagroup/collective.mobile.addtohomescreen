from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.mobile.addtohomescreen',
      version=version,
      description="Plone integration of add-to-home-screen script",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.1",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Environment :: Handhelds/PDA's",
          "Environment :: Web Environment",
          "Intended Audience :: End Users/Desktop",
          "Operating System :: OS Independent",
          "Operating System :: MacOS :: MacOS X",
          "Programming Language :: JavaScript",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Development Status :: 3 - Alpha",
      ],
      keywords='web zope plone add-to-homescreen mobile iphone ipod ipad ios',
      author='Quintagroup',
      author_email='support@quintagroup.com',
      url='https://github.com/quintagroup/collective.mobile.addtohomescreen',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.mobile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
          'tests': [
              'plone.app.testing',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
