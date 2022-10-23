#!/bin/bash

# echo every command and exit if any command fails
set -ex

# update in case this is done on a brand new system that has not updated
sudo apt-get update

sudo apt=get install --yes python3-pip

# install so additional apt repositories can be installed
sudo apt-get install --yes software-properties-common

# add ansible apt repository and install newest Ansible
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install --yes ansible

# execute playbook to setup development environment
ansible-playbook -i hosts dev-env.yml --ask-become-pass "$@"

echo 'Log out and back in for shell changes to take effect'
