#!/usr/bin/env python
# coding: utf-8
"""
Module to create MIDI events.
"""

def notesToMidiString(l):
	"""
	Set the lyrics on the NSX-39

	You can set a single note, or a series of notes.
	The device is capable of holding a string of lyrics
	that it will sequence through as notes are played.
	You can update the lyrics at any time.
	"""
	output = "F0 43 79 09 11 0A 00 "
	output += " ".join(["%2x" % i for i in l])
	output += " F7"
	return output

def noteOn(note, velocity=0x45, channel='0'):
	"""
	Create a MIDI noteon event.

	note is required
	velocity and channel are optional
	channel should be a hex digit character
	"""
	return "9%c %2x %2x" % (channel, note, velocity)

def noteOff(note, velocity=0x45, channel='0'):
	"""
	Create a MIDI noteoff event.

	note is required
	velocity and channel are optional
	channel should be a hex digit character
	"""
	return "8%c %2x %2x" % (channel, note, velocity)

def aftertouch(note, velocity=0x45, channel='0'):
	"""
	Create a MIDI aftertouch event.

	note is required
	velocity and channel are optional
	channel should be a hex digit character
	"""
	return "A%c %2x %2x" % (channel, note, velocity)

def bend(lsb, msb, channel='0'):
	"""
	Create a MIDI pitchbend event

	lsb and msb and required
	channel is optional and should be a hex digit character
	"""
	return "E%c %2x %2x" % (channel, lsb, msb)

