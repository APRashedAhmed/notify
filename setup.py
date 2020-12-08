import versioneer
from setuptools import setup, find_packages

setup(name='notify',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='MIT',
      author='aprashedahmed',
      packages=find_packages(),
      description='Centralized place for programmatic notifications',
      )
