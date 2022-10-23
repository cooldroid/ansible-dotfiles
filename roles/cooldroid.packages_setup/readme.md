Role Name
=========

Installs system packages via apt (Debian) or brew (Mac).

Requirements
------------

On Mac, it is expected that homebrew has been installed.

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

    - hosts: localhost
      roles:
         - { role: packages_setup, tags: ['packages_setup'] }

License
-------

MIT
