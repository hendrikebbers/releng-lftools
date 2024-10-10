############
Installation
############

.. note::

    LFtools requires python3 (3.6+) virtual environment.
    https://virtualenv.pypa.io/en/stable/.
    Not using a virtualenv can have serious negative side effects!


For Install
===========

LFTools is available on pypi. LFtools has migrated to python3, ensure python3
is available your system. To install LFTools, create a virtualenv,
with `pip3 install lftools` in your shell.

MacOS
-----------

On MacOS the following commands will install all needed dependencies by using `brew <https://brew.sh/>`_, setup a virtual environment at ``${HOME}/.virtualenvs`` and installs ``lftools`` in the environment.

.. code-block:: bash

    brew install python@3.12 virtualenv python-setuptools python-packaging python-certifi
    mkdir "${HOME}/.virtualenvs"
    cd "${HOME}/.virtualenvs"
    virtualenv lftools
    source lftools/bin/activate
    pip3 install setuptools
    pip3 install lftools


For Development
===============

Often during development you want to run tests and/or
try code out locally as you change it.  To do this you
need the installation of LFTools to be your local git repo.
After doing `pip3 install -r requirements.txt` issue the
command `pip3 install -e .`
