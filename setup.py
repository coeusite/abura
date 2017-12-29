#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='climate_data_downloader',
      version='0.1.0',
      author_email='coeusite@gmail.com',
      description='Semi-automatic downloader for IGRA2/ISD datasets',
      author='CoeusITE',
      url='https://github.com/coeusite/climate_data_downloader',
      packages=['climate_data_downloader',],
      package_dir={'climate_data_downloader': 'src'},
      )
