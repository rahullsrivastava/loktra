import re
import sys

# regular expression for URI Manipulations
rfc_3986 = re.compile(r"""
           # Parse and capture RFC-3986 Generic URI components.
           ^                                    # anchor to beginning of string
           (?:  (?P<scheme>    [^:/?#\s]+): )?  # capture optional scheme
           (?://(?P<authority>  [^/?#\s]*)  )?  # capture optional authority
                (?P<path>        [^?#\s]*)      # capture required path
           (?:\?(?P<query>        [^#\s]*)  )?  # capture optional query
           (?:\#(?P<fragment>      [^\s]*)  )?  # capture optional fragment
           $                                    # anchor to end of string
           """, re.MULTILINE | re.VERBOSE)
re_domain = re.compile(r"""
           # Pick out top two levels of DNS domain from authority.
           (?P<domain>[^.]+\.[A-Za-z]{2,6})  # $domain: top two domain levels.
           (?::[0-9]*)?                      # Optional port number.
           $                                 # Anchor to end of string.
           """,
                       re.MULTILINE | re.VERBOSE)


class URLExplorer(object):
    """
    URI manipulation to get scheme, domain ,authority of uri
    add/update variable to URI
    """
    def __init__(self):
        pass

    def uri_details(self, url):
        """
        GET Scheme, Domain, Auth of URL
        :return:
        """
        m_uri = rfc_3986.match(url)
        if m_uri and m_uri.group("authority"):
            auth = m_uri.group("authority")
            scheme = m_uri.group("scheme");
            m_domain = re_domain.search(auth)
            if m_domain and m_domain.group("domain"):
                domain = m_domain.group("domain");
        print "scheme :%s"%scheme
        print "domain :%s"%domain
        print "authority: %s"%auth


    def uri_manipulate(self,url, key, value):
        """
        Add/update query  string to URL
        :param var:
        :return:
        """
        m_uri = rfc_3986.match(url)
        if m_uri and m_uri.group("authority"):
            query = m_uri.group("query")
            if query:
                new_url = url.replace(query, key+'='+value)
            else:
                new_url = url + '/' + '?' + key + '=' + value
            print new_url


if __name__ == '__main__':
    argv = sys.argv
    uri = URLExplorer()
    if len(argv) == 4:
        url = argv[1]
        key = argv[2]
        value = argv[3]
        uri.uri_manipulate(url, key, value)
    elif len(argv) ==2:
        url = argv[1]
        uri.uri_details(url)
    else:
        print "please enter URI while running this program"