#!/usr/bin/env python
# coding: utf-8

def notesToMidiString(l):
	output = "F0 43 79 09 11 0A 00 "
	output += " ".join(["%2x" % i for i in l])
	output += " F7"
	return output
