from url_normalize import url_normalize
from urlparse import urlparse

class URL:
  def __init__(self, url):
    self.url = url
    self.cleaned_url = url_normalize(url)

  def isValid(self):
    return self.url == self.cleaned_url

  def getCanonicalized(self):
    url = urlparse(self.cleaned_url)
    return url[0] + '://' + url[1] + url[2]

  def getCleaned(self):
    return self.cleaned_url

  def __len__(self):
    return len(self.cleaned_url)

  def __getitem__(self, index):
    return self.cleaned_url[index]

  # Comparison using normalized url
  def __lt__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid() > other.isValid()
    else:
      return self.cleaned_url < other.cleaned_url

  def __le__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid() > other.isValid()
    else:
      return self.cleaned_url <= other.cleaned_url

  def __gt__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid() < other.isValid()
    else:
      return self.cleaned_url > other.cleaned_url

  def __ge__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid < other.isValid()
    else:
      return self.cleaned_url >= other.cleaned_url

  def __eq__(self, other):
    if self.isValid() != other.isValid():
      return False
    else:
      return self.cleaned_url == other.cleaned_url
