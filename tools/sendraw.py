#!/usr/bin/env python
# coding: utf-8
"""Send a raw message the NSX-39"""

import sys

from pocketmiku.amidi import send

if __name__ == "__main__":
	print "Sending %s" % " ".join(sys.argv[1:])
	send("".join(sys.argv[1:]))
