#!/usr/bin/env python
# coding: utf-8

import time

from amidi import send
from control import noteOn, noteOff, notesToMidiString
from notes import stringToNotes, characters

song_chars = u"nあかばnあかにゃえくすかべてぃJふぁあまいnでるとあまいなふぉてぃないなあnどひずだたくれみんたいん"
song_notes = stringToNotes(song_chars)
song_keys = [70, 70, 70, 65, 74, 74, 74, 70, 70, 70, 70, 74, 77, 77, 77, 75, 74, 72, 72, 72, 72, 72, 72, 74, 75, 75, 75, 74, 72, 74, 74, 70, 70, 70, 70, 74, 74, 72, 65, 69, 69, 72, 72, 70, 70, 70]
song_lengths = [0.75, 0.25, 1, 1, 0.75, 0.25, 1, 1, 0.25, 0.25, 0.25, 0.75, 1.5, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 1.0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1.0, 0.75, 0.25, 0.5, 0.5, 1.0, 0.25, 0.25, 0.25, 0.10, 0.15, 1.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1.0]
song_piano = [1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,0]
song_speed = 0.6

assert len(song_notes) == len(song_lengths) and len(song_lengths) == len(song_keys) and len(song_keys) == len(song_piano)

for i in xrange(0, len(song_notes)):
	print "Note:", song_notes[i], characters[song_notes[i]]
	print "Key:", song_keys[i]
	print "Length:", song_lengths[i]
	send(notesToMidiString([song_notes[i]]))
	send(noteOn(song_keys[i]))

	if song_piano[i]:
		if (i > 0):
			send(noteOff(song_keys[i-1], channel='1'))
		send(noteOn(song_keys[i], channel='1'))
	time.sleep(song_lengths[i] * song_speed)
	if i == len(song_notes) - 1:
		send(noteOff(song_keys[i], 20))
		send(noteOff(song_keys[i], channel='1'))
