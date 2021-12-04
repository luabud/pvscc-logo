import pytest
import unittest
from logo_app import generate_logo_app
import io
import pathlib

class TestFigure(unittest.TestCase):
    def test_generate_figure(self):
        url = "https://code.visualstudio.com/docs/python/python-tutorial"
        mask_path = (
            pathlib.Path(__file__).parent / "logo_app" / "static" / "images" / "python-colored-mask.png"
        )
        # this test fails on purpose. To fix it, replace io.BytesIO with str in the line below.
        self.assertTrue(isinstance(generate_logo_app.generate_fig(url,mask_path), io.BytesIO))
