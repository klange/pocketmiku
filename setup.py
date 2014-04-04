from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

def find_version(*file_paths):
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name="pocketmiku",
    version=find_version('pocketmiku', '__init__.py'),
    description="Tools to configure a Pocket Miku (NSX-39)",
    long_description="""This package provides tools to set the lyrics on and send MIDI events to a Pocket Miku (NSX-39) hardware voice synthesizer.""",

    url='https://github.com/klange/pocketmiku',

    author='Kevin Lange',
    author_email='klange@dakko.us',

    license='University of Illinois/NCSA Open Source License',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia :: Sound/Audio :: MIDI',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'License :: OSI Approved :: University of Illinois/NCSA Open Source License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='miku vocaloid pocketmiku nsx-39 midi audio',

    packages=['pocketmiku'],
    install_requires = [],
)

