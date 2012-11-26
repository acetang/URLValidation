<strong>November 28st Release</strong>
This program reads from a file a list of URLs and display in read order:
<ul>
  <li>Source URL.</li>
  <li>A boolean that says whether or not the URL is valid.</li>
  <li>Canonical URL.</li>
  <li>A boolean that says whether or not the URL is unique.</li>
  <li>A boolean that says whether or not the canonicalized URL is unique.</li>
</ul>

The command for running main.py with this new feature is shown below:

    $python main.py filename

The functions for URL validation, canonicalization and comparison are captured within an URL class. An URL object is 
first created for an URL string from the file. Validation of the URL string is done by calling the isValid() function
in the class. Canonicalization of the URL string is done by calling the getCanonicalized() function. Comparison between
two URL objects can be done using either <, > or ==.

An URL is considered valid if the original URL matches the cleaned URL. We made this assumption to simplify what is
considered valid since the things needed to be considered in cleaned form are fairly standard. We did not want to address
very small issues that may be contained in a non-normalized URL, which some people still accept as valid. We felt the issues
addressed in making sure a url is cleaned eliminates most of the odd things in a url that would make it invalid. 

The URL class cleans URLs using url_normalized.py module implemented by Nikolai Panov. This is a fairly standard
normalized form that covers the cases we were most concerned with. It cleans URLs using the following rules:

<ul>
  <li>Take care of IDN domains.
  <li>Convert the scheme and host to lower case.</li>
  <li>Capitalize letters in escape sequences.</li>
  <li>Decode percent-encoded octets of unreserved characters.</li>
  <li>Remove the default port.</li>
  <li>Remove dot-segments.</li>
  <li>Remove duplicate slashes.</li>
  <li>Remove the "?" when the query is empty.</li>
  <li>Use 'http' schema by default when appropriate.</li>
  <li>For schemes that define a default authority, use an empty authority if the default is desired.</li>
  <li>For schemes that define an empty path to be equivalent to a path of "/", use "/".</li>
  <li>All portions of the URI must be utf-8 encoded NFC from Unicode strings.</li>
</ul>

Therefore our defintion of when a URL is clean, is a URL that abides by the above rules. 
Our definition of a valid URL is one that abides by these rules as well.

The canonical url returned by getCanonicalized() function remove any parameter, query or fragment from the cleaned url.

The comparator of URL class compares first by their validity, where valid URLs come before invalid ones. 
Next, the comparator compare strings of the cleaned URLs using the same rule as string comparison.
The <, >, and == will all be the default string operators since we are treating the URLs as strings.

I have included a unit test file urltest.py which test the functionality of the comparator, validator and canonicalizer
in the URL class.

Note: 
All canonicalized URL are considered as not unique as it is always possible to get the same canonicalized URL
by changing the querys, fragments or parameters of a URL.