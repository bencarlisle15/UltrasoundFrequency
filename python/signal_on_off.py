#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2019 ben.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
import thread
import time
from gnuradio import gr, uhd, blocks
import pmt

class signal_on_off(gr.basic_block):
    """
    docstring for block signal_on_off
    """
    def __init__(self, period, pulse, center_freq):
        gr.basic_block.__init__(self,
            name="signal_on_off",
            in_sig=[],
            out_sig=[])
        self.message_port_register_out(pmt.intern('out1'))
        self.message_port_register_out(pmt.intern('out2'))
        thread.start_new_thread(self.start_frequency_changer, ('Thread-1', period, pulse, center_freq))

    def set_freq(self, center_freq, keep):
        self.message_port_pub(pmt.intern('out1'), pmt.cons(pmt.intern('keep'), pmt.from_bool(not keep)))
        self.message_port_pub(pmt.intern('out2'), pmt.cons(pmt.intern('keep'), pmt.from_bool(keep)))
        # print("*** Turning Signal " + str(not keep) + " ***")

    def start_frequency_changer(self, name, period, pulse, center_freq):
        while True:
            self.set_freq(center_freq, False)
            time.sleep(pulse)
            self.set_freq(center_freq - 5*10**6, True)
            time.sleep(period - pulse)
