import os
import json
from os.path import relpath, join
from setuptools import setup, find_packages

def _load_package_json():
    with open('package.json', 'r') as file:
        return json.loads(file.read())

def _get_package_data(pkg_dir, data_subdir):
    result = []
    for dirpath, _, filenames in os.walk(join(pkg_dir, data_subdir)):
        for filename in filenames:
            filepath = join(dirpath, filename)
            result.append(relpath(filepath, pkg_dir))
    return result

PACKAGE = _load_package_json()

setup(
    name='ppg',
    version=PACKAGE['version'],
    description=PACKAGE['description'],
    long_description=
        PACKAGE['description'] + '\n\nHome page: ',
    author=PACKAGE['author'],
    author_email=PACKAGE['author_email'],
    url=PACKAGE['homepage'],
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
    install_requires=['PyInstaller==6.9.0'],
    extras_require={
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
    license=PACKAGE['license'],
    keywords=PACKAGE['keywords'],
    platforms=['MacOS', 'Windows', 'Debian', 'Fedora', 'CentOS', 'Arch', 'Raspbian'],
    test_suite='tests',
    include_package_data=True,
    data_files=[
        ('ppg/builtin_commands', ['package.json']),
    ],
)
