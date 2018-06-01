__all__ = ["core"]

import TEMPLATE.core.base

def DummySpit():
  return "BLARGH"

def DummySpitBase():
  return TEMPLATE.core.base.DummySpit()
