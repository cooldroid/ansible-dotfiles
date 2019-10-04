import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

NODE_VERSION = '10.15.0'
NVM_VERSION = '0.34.0'


def test_nvm_installed(host):
    test_cmd = 'source /home/ubuntu/.nvm/nvm.sh && nvm --version'

    version = host.check_output('/bin/bash -c "{}"'.format(test_cmd))

    assert version == NVM_VERSION


def test_node_installed(host):
    test_cmd = 'source /home/ubuntu/.nvm/nvm.sh && nvm use "{}"' \
        .format(NODE_VERSION)

    assert host.run_expect([0], '/bin/bash -c "{}"'.format(test_cmd))


def test_npm_packages_installed(host):
    packages = ['diff-so-fancy']

    source_nvm = 'source /home/ubuntu/.nvm/nvm.sh && '
    for package in packages:
        npm_ls = 'npm list --depth 1 --global {}'.format(package)

        test_cmd = source_nvm + npm_ls

        assert host.run_expect([0], '/bin/bash -c "{}"'.format(test_cmd))
