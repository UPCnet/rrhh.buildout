#!/usr/bin/python
#
import logging
import sys
logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

import mechanize

br = mechanize.Browser()
br.add_password("http://localhost:8080/", "admin", "admin", realm="Zope")
br.open("http://localhost:8080/@@reload?action=code")
cj = mechanize.CookieJar()
br.set_cookiejar(cj)
br.select_form(nr=0)
#br.set_handle_refresh(False)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)
#br.set_debug_http(True)
br.submit()
br.close()
