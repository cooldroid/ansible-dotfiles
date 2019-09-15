import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

BAT_VERSION = '0.12.1'
FD_VERSION = '7.2.0'


def test_packages_are_installed(host):
    packages = [
        {'name': 'bat', 'version': BAT_VERSION},
        {'name': 'fd', 'version': FD_VERSION},
        'jq',
        'silversearcher-ag'
    ]

    for package in packages:
        if type(package) is str:
            assert host.package(package).is_installed
        else:
            assert host.package(package['name']).is_installed
            assert host.package(package['name']).version == package['version']
