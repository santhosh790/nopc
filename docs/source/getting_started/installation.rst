Installing nopc
===============

nopc supports Python 3.5+. The recommended way to install nopc is via ``pip``.

.. code-block:: bash

   pip install nopc

.. note:: Depending on your system, you may need to use ``pip3`` to install
          packages for Python 3.

.. caution::
    If you get a ``Permission denied`` error, try installing with sudo permission (on Linux/Mac).

    .. code-block:: bash

        sudo pip install nopc --upgrade

    Another alternative is to try installing with the ``--user`` flag, but you'll need to ensure that the target directory is added to your system ``PATH``.

    .. code-block:: bash

        pip install nopc --upgrade --user

Updating nopc
-------------

nopc can be updated by running:

.. code-block:: bash

   pip install --upgrade nopc

Installing Older Versions
-------------------------

Older versions of nopc can be installed by specifying the version number as
part of the installation command:

.. code-block:: bash

   pip install nopc==0.0.1

