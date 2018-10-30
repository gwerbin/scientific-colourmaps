""" Utility to load Fabio Crameri's scientific colourmaps

Crameri, F. (2018). Scientific colour-maps. Zenodo. http://doi.org/10.5281/zenodo.1243862
Crameri, F. (2018), Geodynamic diagnostics, scientific visualisation and StagLab 3.0, Geosci. Model Dev., 11, 2541-2562, doi:10.5194/gmd-11-2541-2018

As of October 30, 2018:
  - the homepage is http://www.fabiocrameri.ch/colourmaps.php
  - the direct download is http://www.fabiocrameri.ch/resources/ScientificColourMaps4.zip
  - the README file is http://www.fabiocrameri.ch/resources/%2BREADME_ScientificColourmaps.pdf
"""
from functools import lru_cache
from pathlib import Path
from zipfile import ZipFile

import numpy as np
from matplotlib.colors import LinearSegmentedColormap


# http://www.fabiocrameri.ch/colourmaps.php
# http://www.fabiocrameri.ch/resources/%2BREADME_ScientificColourmaps.pdf
@lru_cache(None)
def load_cmap(cmap_name, cmap_path=Path('./ScientificColourMaps4.zip')):
    """ Load a colormap

    Parameters
    ----------
    cmap_name: string
    cmap_path: string or PathLike

    Returns
    -------
    cmap: matplotlib.colors.LinearSegmentedColormap

    Examples
    --------
    import numpy as np
    import matplotlib.pyplot as plt
    from scientific_colourmaps import load_cmap

    plot_data = np.vstack([np.arange(-1, 1, 1/6)[None,:],
                           np.arange(1, -1, -1/6)[None,:]])
    plt.imshow(plot_data, cmap=load_cmap('berlin'))
    plt.show()
    """
    cmap_filename = f'ScientificColourMaps4/{cmap_name}/{cmap_name}.txt'  # not sure if I need to care about Windows slashes

    with ZipFile(cmap_path, 'r') as archive:
        with archive.open(cmap_filename) as cmap_file:
            cmap_data = np.loadtxt(cmap_file)

    return LinearSegmentedColormap.from_list(cmap_name, cmap_data)
