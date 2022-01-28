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

It can be installed either from `PyPI <https://pypi.org/project/solo-epd-loader/>`_ using:

.. code:: bash

    pip install solo-mag-loader

or from `Anaconda <https://anaconda.org/conda-forge/solo-mag-loader/>`_ using:

.. code:: bash

    conda install -c conda-forge solo-mag-loader

Usage
-----

The standard usecase is to utilize the ``mag_load`` function, which
returns Pandas dataframe(s) of the MAG measurements.

.. code:: python

   from solo_mag_loader import mag_load

   df = mag_load(sensor, viewing, level, startdate, enddate, path, autodownload)

Input
~~~~~

-  ``sensor``: ``'ept'``, ``'het'``, or ``'step'`` (string)
-  ``viewing``: ``'sun'``, ``'asun'``, ``''north'``, or ``'south'`` (string); not
   needed for ``sensor = 'step'``
-  ``level``: ``'ll'`` or ``'l2'`` (string)
-  ``startdate``, ``enddate``: YYYYMMDD, e.g., 20210415 (integer) (if no
   ``enddate`` is provided, ``enddate = startdate`` will be used)
-  ``path``: directory in which Solar Orbiter data is/should be
   organized; e.g. ``'/home/userxyz/solo/data/'`` (string). See `Data folder structure`_ for more details.
-  ``autodownload``: if ``True`` will try to download missing data files
   from SOAR (bolean)

Return
~~~~~~

-  For ``sensor`` = ``'ept'`` or ``'het'``:

   1. Pandas dataframe with proton fluxes and errors (for EPT also alpha
      particles) in ‘particles / (s cm^2 sr MeV)’
   2. Pandas dataframe with electron fluxes and errors in ‘particles /
      (s cm^2 sr MeV)’
   3. Dictionary with energy information for all particles:

      -  String with energy channel info
      -  Value of lower energy bin edge in MeV
      -  Value of energy bin width in MeV

-  For ``sensor`` = ``'step'``:

   1. Pandas dataframe with fluxes and errors in ‘particles / (s cm^2 sr
      MeV)’
   2. Dictionary with energy information for all particles:

      -  String with energy channel info
      -  Value of lower energy bin edge in MeV
      -  Value of energy bin width in MeV

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
