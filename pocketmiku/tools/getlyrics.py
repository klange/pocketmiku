#!/usr/bin/env python
# coding: utf-8

import sys

from pocketmiku.notes import characters
from pocketmiku.control import sysExString
from pocketmiku.amidi import sendAndGetResponse

def getLyricsStringForChannel(channel=0):
    results = sendAndGetResponse(sysExString(["0F %2x" % channel])).strip()
    results = results.split("\n")
    for result in results:
        if not result.startswith("F0 43 79 09 11 1F"):
            continue
        result = result.split(" ")[7:-1]
        output = u""
        for i in result:
            d = int(i, 16)
            output += characters[d]
        return output

if __name__ == "__main__":
    for i in xrange(0, 16):
        print i, getLyricsStringForChannel(i)

