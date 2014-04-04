#!/usr/bin/env python
# coding: utf-8

from subprocess import call, check_output

hardware_port = None

def detectHardwarePort():
	global hardware_port
	devices = check_output(['amidi', '-l'])
	for line in devices.split('\n'):
		if line.startswith('IO') and "NSX-39" in line:
			hw = line[line.index('hw'):]
			hw = hw[:hw.index(' ')]
			hardware_port = hw
			return
	raise ValueError("Couldn't find an NSX-39 T-T")

def send(s):
	if not hardware_port:
		detectHardwarePort()
	call(['amidi', '-p', hardware_port, '-S', s])

