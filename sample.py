#!/usr/bin/env python
# coding: utf-8

import time

from amidi import send
from control import noteOn, noteOff, notesToMidiString
from notes import stringToNotes

song_chars = u"きみがあよおわちよにいいやちよにさざれいしのいわおとなりてこけのむうすうまああで"
song_notes = stringToNotes(song_chars)
song_keys = [62, 60, 62, 64, 67, 64, 62, 64, 67, 69, 67, 69, 74, 71, 69, 67, 64, 67, 69, 74, 72, 74, 64, 67, 69, 67, 64, 67, 62, 69, 72, 74, 72, 74, 69, 67, 69, 67, 64, 62]
song_lengths = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1.5, 0.5, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0.5, 0.5, 2]

assert len(song_notes) == len(song_lengths) and len(song_lengths) == len(song_keys)

for i in xrange(0, len(song_notes)):
	print "Note:", song_notes[i]
	print "Key:", song_keys[i]
	print "Length:", song_lengths[i]
	send(notesToMidiString([song_notes[i]]))
	send(noteOn(song_keys[i]))
	time.sleep(song_lengths[i] * 0.4)
	send(noteOff(song_keys[i], 20))
