#!/usr/bin/env python
# coding: utf-8

import time

from pocketmiku.amidi import send
from pocketmiku.control import noteOn, noteOff, notesToMidiString
from pocketmiku.notes import characters

scale = [60, 62, 64, 65, 67, 69, 71, 72]
names = ['C','D','E','F','G','A','B','C']

for i in xrange(0, 0x80):
    print "Playing a %s on a %s." % (characters[i], names[i % len(names)])
    send(notesToMidiString([i]))
    send(noteOn(scale[i % len(names)]))
    time.sleep(0.5)
    send(noteOff(scale[i % len(names)]))
