Installing Correos express
==============

Prerequisites
-------------

 * Python (http://www.python.org/)

Installation
------------

Once you've downloaded and unpacked the asm source release, enter the
directory where the archive was unpacked, and run:

    python setup.py install

    or

    pip install git@github.com:aldovillagra/python-correosexpress.git#egg=correosexpress

Note that you may need administrator/root privileges for this step, as
this command will by default attempt to install module to the Python
site-packages directory on your system.

For advanced options, please refer to the easy_install and/or the distutils
documentation:

  http://peak.telecommunity.com/DevCenter/EasyInstall
  http://docs.python.org/inst/inst.html