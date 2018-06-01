from unittest import TestCase
import TEMPLATE

class TestBase(TestCase):
  def test_root(self):
    s = TEMPLATE.DummySpit()
    self.assertTrue(s == "BLARGH")

  def test_base(self):
    s = TEMPLATE.DummySpitBase()
    self.assertTrue(s == "BLARGH_BASE")
