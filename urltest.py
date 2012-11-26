import unittest
from url import URL

class TestURLCanonicalizer(unittest.TestCase):
  canonical = "http://en.wikipedia.org/wiki/Unit_testing"
  notcanonical = "http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations"

  # Test that URL Canonicalizer does not change a canonical URL
  def test_canonical_url(self):
    url = URL(self.canonical)
    self.assertEqual(url.getCanonicalized(), self.canonical)

  # Test that URL Canonicalizer correctly canonicalized an URL.
  def test_not_canonical_url(self):
    url = URL(self.notcanonical)
    self.assertEqual(url.getCanonicalized(), self.canonical)

class TestURLValidator(unittest.TestCase):
  canonical = "http://en.wikipedia.org/wiki/Unit_testing"
  notcanonical = "http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations"
  invalid = "en.wikipedia.org/wiki/Unit_testing"

  def test_valid_canonical(self):
    url = URL(self.canonical)
    self.assertTrue(url.isValid())

  def test_valid_not_canonical(self):
    url = URL(self.notcanonical)
    self.assertTrue(url.isValid())

  def test_invalid(self):
    url = URL(self.invalid)
    self.assertFalse(url.isValid())

class TestURLComparator(unittest.TestCase):
  canonical = "http://en.wikipedia.org/wiki/Unit_testing"
  notcanonical = "http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations"
  invalid = "en.wikipedia.org/wiki/Unit_testing"

  def test_valid_with_valid_lt(self):
    url1 = URL(self.canonical)
    url2 = URL(self.notcanonical)
    self.assertTrue(url1 < url2)

  def test_valid_with_valid_gt(self):
    url1 = URL(self.canonical)
    url2 = URL(self.notcanonical)
    self.assertTrue(url2 > url1)

  def test_valid_with_valid_eq(self):
    url1 = URL(self.canonical)
    url2 = URL(self.canonical)
    self.assertTrue(url1 == url2)

  def test_valid_with_invalid_lt(self):
    url1 = URL(self.canonical)
    url2 = URL(self.invalid)
    self.assertTrue(url1 < url2)

  def test_valid_with_invalid_gt(self):
    url1 = URL(self.canonical)
    url2 = URL(self.invalid)
    self.assertTrue(url2 > url1)

  def test_valid_with_invalid_eq(self):
    url1 = URL(self.canonical)
    url2 = URL(self.invalid)
    self.assertFalse(url1 == url2)

if __name__ == '__main__':
  unittest.main()
