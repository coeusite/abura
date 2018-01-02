
from src import fetch_history
fetch_history()

from src import Abura_IGRA2
# IGRA2 Downloader
downloader = Abura_IGRA2('IGRA2')
downloader.run(
    stations = ['CHM00056294']) # ChengDu

# IGRA2 Derived Downloader
downloader = Abura_IGRA2('IGRA2 DRVD')
downloader.run(
    stations = ['CHM00056294']) # ChengDu

from src import Abura_ISD
# ISD Downloader
downloader = Abura_ISD('ISD')
downloader.run(
    stations = ['562940-99999'], # ChengDu
    years = [2013, 2014, 2015, 2016, 2017])

# ISD Lite Downloader
downloader = Abura_ISD('ISD LITE')
downloader.run(
    stations = ['562940-99999'], # ChengDu
    years = [2013, 2014, 2015, 2016, 2017])

# GSOD Downloader
downloader = Abura_ISD('GSOD')
downloader.run(
    stations = ['562940-99999'], # ChengDu
    years = [2013, 2014, 2015, 2016, 2017])
