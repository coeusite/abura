#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re
import wget
#import pandas as pd, numpy as np

import time, urllib

from pdb import set_trace as bp
from datetime import date

from .constant import DEFAULT_YEARS, DEFAULT_GAP, DEFAULT_ERROR_GAP
from .constant import ISD_PATH_HISTORY, IGRA2_PATH_HISTORY
from .constant import ISD_URL_FORMAT, ISD_LITE_URL_FORMAT, GSOD_URL_FORMAT
from .constant import IGRA2_URL_FORMAT, IGRA2_DRVD_URL_FORMAT

class Abura_Base(object):

    ''' primary object for downloading climate data '''
    def __init__(self):
        ''' init '''
        self.stations = []
        self.urls = []
        self.years = DEFAULT_YEARS
        self.data_folder = 'data/'
        return

    def wget(self, url, file_path, force_refresh=False):
        ''' wget URL to file_path '''
        # 文件存在且不要求强制更新，则跳过文件；否则删除文件重新下载
        if os.path.isfile(file_path):
            if not(force_refresh):
                print('skip...',file_path)
                return
            else:
                print('refreshing...',file_path)
                os.remove(file_path)
        else:
            print('downloading...', file_path)
        try:
            wget.download(url, out=file_path)
            time.sleep(DEFAULT_GAP)
        except urllib.error.URLError as err:
            if "ftp error: error_perm('530" in err.reason:
                print('530 Error...', file_path) # Maximum number of connections exceeded.
                time.sleep(DEFAULT_ERROR_GAP)
                self.wget(url, file_path, force_refresh=True)
            else:
                print('URLError:', err.reason)
            pass
        return

    def set_stations(self, stations):
        ''' stations should be a list of str '''
        # set stations
        if isinstance(stations, list):
            self.stations = stations
        else:
            self.stations = [str(stations)]
        return

    def set_years(self, years):
        ''' years should be a list of str or int '''
        # set stations
        if isinstance(years, list):
            self.years = years
        else:
            self.years = [years]
        return

    def run(self, stations = None, years = None):
        # Part 0: Setting parameters
        # stations
        if stations is not None:
            self.set_stations(stations)
        # years
        if years is not None:
            self.set_years(years)
        # check output folder 不存在时自动创建
        if not os.path.isdir(self.data_folder):
            os.makedirs(self.data_folder)
        # Part 1: Parse URLs
        self.parse_urls()
        # Part 2: Download files
        self.download()
        return

class Abura_IGRA2(Abura_Base):
    ''' object for downloading IGRA2 files '''

    def __init__(self, mode = 'IGRA2'):
        ''' init '''
        super().__init__()
        # 模式 大写字母
        mode = mode.upper()
        if mode == 'IGRA2 DRVD':
            self.url_format = IGRA2_DRVD_URL_FORMAT
            self.data_folder = 'data/igra2-drvd/'
        else:
            if mode != 'IGRA2':
                print("Incorrect mode! Use IGRA2 instead...")
            self.url_format = IGRA2_URL_FORMAT
            self.data_folder = 'data/igra2/'

    def parse_urls(self):
        ''' Part 1: parse URLs '''
        print('parsing IGRA2 URLs......')
        self.urls = []
        for station in self.stations:
            url = self.url_format.format(station=station)
            self.urls.append(url)
        return

    def download(self):
        '''  Part 2: download files '''
        for i in range(len(self.urls)):
            url = self.urls[i]
            file_name = os.path.basename(url)
            file_path = self.data_folder + file_name
            self.wget(url, file_path, force_refresh=True)
        return

class Abura_ISD(Abura_Base):
    ''' object for downloading Integrated Surface Database (ISD) files '''

    def __init__(self, mode = 'ISD'):
        ''' init '''
        super().__init__()
        # 模式 大写字母
        mode = mode.upper()
        if mode == 'ISD LITE':
            self.url_format = ISD_LITE_URL_FORMAT
            self.data_folder = 'data/isd-lite/'
        elif mode == 'GSOD':
            self.url_format = GSOD_URL_FORMAT
            self.data_folder = 'data/gsod/'
        else:
            if mode != 'ISD':
                print("Incorrect mode! Use ISD instead...")
            self.url_format = ISD_URL_FORMAT
            self.data_folder = 'data/isd/'
        #history = pd.read_csv(PATH_ISD_HISTORY)
        #history.index = history.USAF.astype(str) + '-' + history.WBAN.astype(str)
        #self.history = history
        return

    def parse_urls(self):
        ''' Part 1: parse URLs '''
        print('parsing Integrated Surface Database (ISD) URLs......')
        self.urls = []
        for station in self.stations:
            for year in self.years:
                url = self.url_format.format(station=station, year=year)
                self.urls.append(url)
        return

    def download(self):
        '''  Part 2: download files '''
        for i in range(len(self.urls)):
            url = self.urls[i]
            file_name = os.path.basename(url)
            file_path = self.data_folder + file_name
            match_current_year = re.match('.*-{}\.gz'.format(date.today().year), file_name)
            force_refresh = (match_current_year is not None)
            self.wget(url, file_path, force_refresh)
        return
