from os.path import relpath, join
from setuptools import setup, find_packages

import os

def _get_package_data(pkg_dir, data_subdir):
    result = []
    for dirpath, _, filenames in os.walk(join(pkg_dir, data_subdir)):
        for filename in filenames:
            filepath = join(dirpath, filename)
            result.append(relpath(filepath, pkg_dir))
    return result

description = 'Create cross-platform desktop applications with Python and Qt5/Qt6'
setup(
    name='ppg',
    # Also update ppg/_defaults/requirements/base.txt when you change this:
    version='1.0.3',
    description=description,
    long_description=
        description + '\n\nHome page: ',
    author='Luis Alfredo Reyes',
    author_email='',
    url='',
    packages=find_packages(exclude=('tests', 'tests.*')),
    package_data={
        'ppg': _get_package_data('ppg', '_defaults'),
        'ppg.builtin_commands':
            _get_package_data('ppg/builtin_commands', 'project_template'),
        'ppg.builtin_commands._gpg':
            ['Dockerfile', 'genkey.sh', 'gpg-agent.conf'],
        'ppg.installer.mac': _get_package_data(
            'ppg/installer/mac', 'create-dmg'
        )
    },
    install_requires=['PyInstaller>=4.5.1'],
    extras_require={
        # Also update requirements.txt when you change this:
        'licensing': ['rsa>=3.4.2'],
        'sentry': ['sentry-sdk>=0.6.6'],
        'upload': ['boto3']
    },
    classifiers=[
        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Operating System :: OS Independent',

        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': ['ppg=ppg.__main__:_main']
    },
    license='GPLv3 or later',
    keywords=['PyQt', 'PyQt5', 'PyQt6', 'PySide2', 'PySide6', 'Qt5', 'Qt6'],
    platforms=['MacOS', 'Windows', 'Debian', 'Fedora', 'CentOS', 'Arch', 'Raspbian'],
    test_suite='tests'
)
