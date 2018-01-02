#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re
import wget

from .constant import ISD_PATH_HISTORY, IGRA2_PATH_HISTORY

def fetch_history(force_refresh=False):
    ''' Fetch URLs '''
    fetch_ISD(force_refresh)
    fetch_IGRA2(force_refresh)
    return

def fetch_ISD(force_refresh=False):
    ''' Fetch ISD history '''
    # auto check
    if os.path.isfile(ISD_PATH_HISTORY) and not(force_refresh):
        print('skip ISD history fetching')
        return
    # history
    print('fetching Integrated Surface Database (ISD) history......')
    wget.download('ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-history.csv',
        out=ISD_PATH_HISTORY)
    return

def fetch_IGRA2(force_refresh=False):
    ''' Fetch IGRA2 history '''
    # auto check
    if os.path.isfile(IGRA2_PATH_HISTORY) and not(force_refresh):
        print('skip IGRA2 history fetching')
        return
    # history
    print('fetching Integrated Surface Database (ISD) history......')
    wget.download('ftp://ftp.ncdc.noaa.gov/pub/data/igra/igra2-station-list.txt',
        out=IGRA2_PATH_HISTORY)
    return
