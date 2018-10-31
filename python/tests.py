from unittest import TestCase
from matplotlib.colors import LinearSegmentedColormap
from scientific_colourmaps import load_cmap, list_cmaps, __version__

cmap_path = '../ScientificColourMaps4.zip'


class TestCaseMain(TestCase):
    def test_main(self):
        for cmap_name in list_cmaps(cmap_path):
            cmap = load_cmap(cmap_name, cmap_path)
            self.assertIsInstance(cmap, LinearSegmentedColormap)


class TestAlias(TestCase):
    def test_import(self):
        import scientific_colormaps
        self.assertTrue(hasattr(scientific_colormaps, 'load_cmap'))
        self.assertTrue(hasattr(scientific_colormaps, 'list_cmaps'))
        self.assertEqual(scientific_colormaps.__version__, __version__)
        self.assertEqual(scientific_colormaps.list_cmaps(cmap_path), list_cmaps(cmap_path))

