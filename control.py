#!/usr/bin/env python
# coding: utf-8

def notesToMidiString(l):
	output = "F0 43 79 09 11 0A 00 "
	output += " ".join(["%2x" % i for i in l])
	output += " F7"
	return output

def noteOn(note, velocity=0x45, channel='0'):
	return "9%c %2x %2x" % (channel, note, velocity)

def noteOff(note, velocity=0x45, channel='0'):
	return "8%c %2x %2x" % (channel, note, velocity)

def aftertouch(note, velocity=0x45, channel='0'):
	return "A%c %2x %2x" % (channel, note, velocity)

def bend(lsb, msb, channel='0'):
	return "E%c %2x %2x" % (channel, lsb, msb)

