import pytest
import unittest
import generate_logo
import io

class TestFigure(unittest.TestCase):
    def test_generate_figure(self):
        self.assertTrue(isinstance(generate_logo.generate_fig(), io.BytesIO))
