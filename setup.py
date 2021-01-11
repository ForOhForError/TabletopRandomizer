import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ttrando',
     version='0.0.1',
     author="ForOhForError",
     description="CLI Utility for Tabletop RPG Randomizer",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     install_requires=[],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     py_modules=['ttrando'],
     entry_points={'console_scripts': ['ttrando = ttrando:main']},
 )
