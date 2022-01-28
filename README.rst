solo-epd-loader
===============

Python data loader for Solar Orbiter's (SolO) MAG instrument. At the moment provides level 2 (l2) obtained by SunPy through CDF files from CDAWeb.

Not working at the moment: `level='ll'` and `frame='VSO'` 

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

   startdate = 20210711
   enddate = 20210712 
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
