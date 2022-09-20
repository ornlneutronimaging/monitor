"""Information and settings for setuptools.setup(). Now the package can be installed with 'pip install .'."""
from setuptools import setup, find_packages
import versioneer

setup(name='monitor',
      version=versioneer.get_version(),
      description='User interface to monitor data reduction.',
      url='',
      author='Jean Bilheux, Venkatrishnan (Venkat) Singanallur, Shimin Tang',
      author_email='bilheuxjm@ornl.gov, venkatakrisv@ornl.gov, tangs@ornl.gov ',
      license='',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      scripts=["scripts/monitor"],
      extras_require=dict(tests=['pytest']),
      zip_safe=False)
