# Colormaps in Matplotlib

## Installation

```bash
pip install scientific-colourmaps
```

or

```bash
conda install -c gwerbin scientific-colourmaps
```

## API

- *module* `scientific_colourmaps`
  - *function* `load_cmap`
    - *arg* `cmap_name`: string. Required.
    - *kwarg* `cmap_path`: string or `os.PathLike`. Optional; default: `cmap_path=CMAP_DEFAULT_PATH` 
    - *return*: instance of `matplotlib.colors.LinearSegmentedColormap`.
  - *function* `list_cmaps`
    - *kwarg* `cmap_path`: string or `os.PathLike`. Optional; default: `cmap_path=CMAP_DEFAULT_PATH` 
    - *return* set of strings, containing available cmap names
  - *variable* `CMAP_DEFAULT_PATH`, instance of `pathlib.Path`
    - value: `pathlib.Path('./ScientificColourMaps4.zip')`
- *module* `scientific_colormaps`, alias of `scientific_colourmaps` for United-States-of-American developers.

## Example

In the shell:

```bash
wget http://www.fabiocrameri.ch/resources/ScientificColourMaps4.zip
```

In Python:

```python
import numpy as np
import matplotlib.pyplot as plt
from scientific_colourmaps import load_cmap

# Make some fake data to plot
plot_data = np.randn(50, 50)

# Plot using the "nuuk" colormap
cmap_nuuk = load_cmap('nuuk')
plt.imshow(plot_data, cmap=cmap_nuuk)
plt.colorbar()
plt.show()
```
