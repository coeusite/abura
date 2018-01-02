Semi-auto downloader for IGRA2 & ISD datasets
--------------------------------

Installing
-------------------------------
If you're a python and pip user, you can install the current development version with:

```
sudo pip install git+https://github.com/coeusite/climate_data_downloader.git
```

or install it locally with:

```
pip install --user git+https://github.com/coeusite/climate_data_downloader.git
```

To upgrade the parser:
```
pip install --user --force-reinstall --upgrade git+https://github.com/coeusite/climate_data_downloader.git
```

Dependency
------------------------------
This module depends on:
* pandas (0.18.1)
* numpy (1.11.1)

Please update these packages to the latest edition.


Using
------------------------------
Using the module should be pretty straightforward. Here's an example:
```

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

```

Developing
--------------------------------
Testing scripts have not been implemented yet.


Contact
--------------------------------
For further questions, please open an issue or contact CoeusITE (coeusite@gmail.com)
