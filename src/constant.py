#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DEFAULT_YEARS = [2013, 2014, 2015, 2016, 2017]
DEFAULT_GAP = 5 # 5 seconds
DEFAULT_ERROR_GAP = 30

ISD_PATH_HISTORY = 'data/isd-history.csv'
IGRA2_PATH_HISTORY = 'data/igra2-station-list.csv'

ISD_URL_FORMAT      = 'ftp://ftp.ncdc.noaa.gov/pub/data/noaa/{year:04d}/{station}-{year:04d}.gz'
ISD_LITE_URL_FORMAT = 'ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-lite/{year:04d}/{station}-{year:04d}.gz'
GSOD_URL_FORMAT     = 'ftp://ftp.ncdc.noaa.gov/pub/data/gsod/{year:04d}/{station}-{year:04d}.op.gz'

IGRA2_URL_FORMAT      = "ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/data-por/{station}-data.txt.zip"
IGRA2_DRVD_URL_FORMAT = "ftp://ftp.ncdc.noaa.gov/pub/data/igra/derived/derived-por/{station}-drvd.txt.zip"
