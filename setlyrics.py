#!/usr/bin/env python
# coding: utf-8

import sys

from notes import stringToNotes
from control import notesToMidiString
from amidi import send

if __name__ == "__main__":
	print u"Setting lyrics to %s" % sys.argv[1].decode('utf-8')
	values = stringToNotes(sys.argv[1].decode('utf-8'))
	print notesToMidiString(values)
	send(notesToMidiString(values))
	print "%d note(s)" % len(values)

