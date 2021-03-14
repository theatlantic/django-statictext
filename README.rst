Django StaticText
=================

Small pieces of static text and links for use with django.


Notes
=====

* version 1.x will be the last version to support Python < 3.4
* version 1.0.0 has added a BSD license (see LICENSE file)
* version 2.0.0 support Python 3.7+ and Django>=2.2,<4.0 only

Testing
=======

Local testing assumes `pyenv <https://github.com/pyenv/pyenv>`_ is installed.

Grab the code::

    git clone git@github.com:theatlantic/django-statictext.git
    cd django-statictext

Specify the Python versions you will be testing with and set up
`tox <https://tox.readthedocs.io/en/latest/`>_

::

    pyenv local 3.7.3 3.8.0
    python3 -m venv venv
    . venv/bin/activate
    pip install tox

Now run all the unit tests::

    tox


Some other common tox usages:

- List test environments: ``tox -lv``
- List all environments with descriptions: ``tox -av``
