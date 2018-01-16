from setuptools import setup, find_packages

setup(name='bpynodes_lib',
      version='1.0.2',
      description='Blender Python Nodes extension that provides a python library for creating Python Node systems',
      url='https://gitlab.com/blenderone/bpynodes_lib1',
      author='Jared Webber',
      author_email='info@onelvxe.com',
      license='GNU GPLv3',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      keywords='blender bpy nodes custom pynodes',
      python_requires='~=3.5',
      #install_requires=['setuptools', 'wheel', 'requests', 'numpy'],
      zip_safe=False)