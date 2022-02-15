# Licensed under a 3-clause BSD style license - see LICENSE.rst

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass  # package is not installed

from sunpy.net import Fido
from sunpy.net import attrs as a
from sunpy.timeseries import TimeSeries


def _date2str(date):
    year = str(date)[0:4]
    month = str(date)[4:6]
    day = str(date)[6:8]
    return year+'/'+month+'/'+day


def mag_load(startdate, enddate, level='l2', type='normal', frame='rtn'):
    """
    Load SolO/MAG data

    Load-in data for Solar Orbiter/MAG sensor. Supports level 2 and low latency
    data provided by ESA's Solar Orbiter Archive. Optionally downloads missing
    data directly. Returns data as Pandas dataframe.

    Parameters
    ----------
    startdate : yyyymmdd (int)
        Provides year (yyyy), month (mm) and day (dd) of the start date as one
        combined integer; fill empty positions with zeros, e.g. '20210415'
    enddate : yyyymmdd (int)
        Provides year (yyyy), month (mm) and day (dd) of the end date as one
        combined integer; fill empty positions with zeros, e.g. '20210415'.
        (enddate must be 1 day after startdate!)
    level : {'l2', 'll'}, optional
        Defines level of data product: level 2 ('l2') or low-latency ('ll').
        By default 'l2'.
    type : {'normal', 'normal-1-minute', or 'burst'}, optional
        By default 'normal'.
    frame : {'rtn', 'srf', or 'vso'}, optional
        Coordinate frame of MAG data. By default 'rtn'.

    Returns
    -------
    Pandas dataframe with fluxes and errors in 'particles / (s cm^2 sr MeV)'
    """
    if type == 'normal-1-minute' and frame == 'srf':
        raise Exception("For SRF frame only 'normal' or 'burst' data type available!")
    
    if type == 'normal-1-min':
        type = 'normal-1-minute'

    if level == 'll' or level == 'LL':
        level = 'll02'
        data_id = 'SOLO_'+level.upper()+'_MAG'
    else:
        data_id = 'SOLO_'+level.upper()+'_MAG-'+frame.upper()+'-'+type.upper()

    trange = a.Time(_date2str(startdate), _date2str(enddate))
    dataset = a.cdaweb.Dataset(data_id)
    result = Fido.search(trange, dataset)
    files = Fido.fetch(result)

    solo_mag = TimeSeries(files, concatenate=True)
    df_solo_mag = solo_mag.to_dataframe()
    return df_solo_mag


# VSO, LL02 not working
