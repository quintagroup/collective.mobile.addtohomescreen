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
        "Programming Language :: Python",
        'License :: OSI Approved :: GNU General Public License (GPL)',
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
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
