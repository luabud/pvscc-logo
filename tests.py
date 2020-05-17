import pytest
import unittest
from logo_app import generate_logo
import io
import pathlib

class TestFigure(unittest.TestCase):
    def test_generate_figure(self):
        url = "https://code.visualstudio.com/docs/python/python-tutorial"
        mask_path = (
            pathlib.Path(__file__).parent / "logo_app" / "static" / "images" / "python-colored-mask.png"
        )
        # this tests fails on purpose. To fix it, replace io.BytesIO with str in the line below
        self.assertTrue(isinstance(generate_logo.generate_fig(url,mask_path), io.BytesIO))
