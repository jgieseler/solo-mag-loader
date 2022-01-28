solo-epd-loader
===============

|pypi Version| |conda version| |license| |python version|

.. |pypi Version| image:: https://img.shields.io/pypi/v/solo-mag-loader?style=flat&logo=pypi
   :target: https://pypi.org/project/solo-mag-loader/
.. |conda version| image:: https://img.shields.io/conda/vn/conda-forge/solo-mag-loader?style=flat&logo=anaconda
   :target: https://anaconda.org/conda-forge/solo-mag-loader/
.. |license| image:: https://img.shields.io/conda/l/conda-forge/solo-mag-loader?style=flat
   :target: https://github.com/jgieseler/solo-mag-loader/blob/main/LICENSE.rst
.. |python version| image:: https://img.shields.io/pypi/pyversions/solo-mag-loader?style=flat&logo=python

Python data loader for Solar Orbiter's (SolO) MAG instrument. At the moment provides level 2 (l2) and low latency (ll) data obtained by SunPy through CDF files from CDAWeb.

**Please always refer to the** `official MAG data description <https://issues.cosmos.esa.int/solarorbiterwiki/display/SOSP/Archive+Support+Data#ArchiveSupportData-MAGInstrument>`_ **before using the data!**

Installation
------------

solo_mag_loader requires python >= 3.6 and SunPy >= 3.1.3

It can be installed from this repository using pip:

.. code:: bash

    pip install git+https://github.com/jgieseler/solo-mag-loader

Usage
-----

The standard usecase is to utilize the ``mag_load`` function, which
returns Pandas dataframe(s) of the MAG measurements.

.. code:: python

   from solo_mag_loader import mag_load

   df = mag_load(startdate, enddate, level='l2', type='normal', frame='rtn')


Data folder structure
---------------------

All data files are automatically saved in a SunPy subfolder of the current user home directory.


License
-------

This project is Copyright (c) Jan Gieseler and licensed under
the terms of the BSD 3-clause license. This package is based upon
the `Openastronomy packaging guide <https://github.com/OpenAstronomy/packaging-guide>`_
which is licensed under the BSD 3-clause licence. See the licenses folder for
more information.

Acknowledgements
----------------

The development of this software has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 101004159 (SERPENTINE).
