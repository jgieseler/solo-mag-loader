solo-mag-loader
===============

Python data loader for Solar Orbiter's (SolO) MAG instrument. At the moment provides level 2 (l2) obtained by SunPy through CDF files from CDAWeb.

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
   df = mag_load(startdate, enddate, level='l2', type='normal', frame='rtn', path=None)

Input
~~~~~

-  ``startdate``, ``enddate``: Datetime object (e.g., dt.date(2021,12,31) or dt.datetime(2021,4,15)), "standard"  datetime string (e.g., "2021/04/15") or integer of the form yyyymmdd with empty positions filled with zeros, e.g. '20210415' (enddate must be later than startdate)
-  ``level``: ``'l2'`` or ``'ll'`` (string). Defines level of data product: level 2 ('l2') or low-latency ('ll'). By default 'l2'
-  ``type``: ``'normal'``, ``'normal-1-minute'``, or ``'burst'`` (string), optional. By default 'normal'.
-  ``frame``: ``'rtn'``, ``'srf'``, or ``'vso'`` (string), optional. Coordinate frame of MAG data. By default 'rtn'.
-  ``path``: String, optional. Local path for storing downloaded data, e.g. ``path='data/solo/mag/'``. By default `None`. Default setting saves data according to `sunpy's Fido standards <https://docs.sunpy.org/en/stable/guide/acquiring_data/fido.html#downloading-data>`_.


``level='ll'`` and ``frame='VSO'`` not working at the moment!

Return
~~~~~~

-  Pandas data frame


Data folder structure
---------------------

All data files are automatically saved in a SunPy subfolder of the current user home directory.


License
-------

This project is Copyright (c) Jan Gieseler and licensed under
the terms of the BSD 3-clause license. This package is based upon
the `Openastronomy packaging guide <https://github.com/OpenAstronomy/packaging-guide>`_
which is licensed under the BSD 3-clause license. See the licenses folder for
more information.

Acknowledgements
----------------

The development of this software has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 101004159 (SERPENTINE).
