import sys

from url import URL

def get_strings(f):
  strings = []
  line = f.readline()
  while len(line) > 0:
    # do not add empty line
    if len(line) > 1:
      strings.append(line[:len(line) - 1])
    line = f.readline()
  return strings

if __name__ == "__main__":

  filename = None
  if len(sys.argv) is not 2:
    print 'Usage: python main.py filename'
    exit(1)

  inputfile = open(sys.argv[1])

  strings = get_strings(inputfile)
  urls = [URL(x) for x in strings]
  for url in urls:
    print('Source: ' + url.url)
    print('Valid: ' + str(url.isValid()))
    print('Canonical: ' + url.getCanonicalized())
    print('Source unique: ' + str(url.getCanonicalized() != url.getCleaned()))
    print('Canonicalized URL unique: False')
