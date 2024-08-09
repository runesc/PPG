from ppg import path, SETTINGS
from ppg.freeze import _generate_resources, run_pyinstaller
from ppg.resources import get_icons
from os import makedirs, unlink, rename, symlink
from os.path import exists
from shutil import copy, rmtree
from subprocess import run

def freeze_mac(debug=False):
    if not exists(path('target/Icon.icns')):
        _generate_iconset()
        run(['iconutil', '-c', 'icns', path('target/Icon.iconset')], check=True)
    args = []
    if not (debug or SETTINGS['show_console_window']):
        args.append('--windowed')
    args.extend(['--icon', path('target/Icon.icns')])
    bundle_identifier = SETTINGS['mac_bundle_identifier']
    if bundle_identifier:
        args.extend([
            '--osx-bundle-identifier', bundle_identifier
        ])
    run_pyinstaller(args, debug)
    _remove_unwanted_pyinstaller_files()
    _generate_resources()

def _generate_iconset():
    makedirs(path('target/Icon.iconset'), exist_ok=True)
    for size, scale, icon_path in get_icons():
        dest_name = 'icon_%dx%d' % (size, size)
        if scale != 1:
            dest_name += '@%dx' % scale
        dest_name += '.png'
        copy(icon_path, path('target/Icon.iconset/' + dest_name))

def _remove_unwanted_pyinstaller_files():
    for unwanted in ('include', 'lib', 'lib2to3'):
        try:
            unlink(path('${freeze_dir}/Contents/MacOS/' + unwanted))
        except FileNotFoundError:
            pass
        try:
            rmtree(path('${freeze_dir}/Contents/Resources/' + unwanted))
        except FileNotFoundError:
            pass

