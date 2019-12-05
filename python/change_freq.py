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

class change_freq(gr.basic_block):
    """
    docstring for block change_freq
    """
    def __init__(self, change_time, start, current, end, step, reverse):
        gr.basic_block.__init__(self,
            name="change_freq",
            in_sig=[],
            out_sig=[])
        self.message_port_register_out(pmt.intern('center_freq'))
        thread.start_new_thread(self.start_frequency_changer, ('Thread-1', change_time, start, current, end, step, reverse))

    def set_freq(self, center_freq):
        self.message_port_pub(pmt.intern('center_freq'), pmt.cons(pmt.intern('freq'), pmt.from_double(center_freq)))
        print("*** Changing frequency to " + str(center_freq) + " ***")

    def start_frequency_changer(self, name, change_time, start, current, end, step, reverse):
        center_freq = current
        reversing = False
        while True:
            self.set_freq(center_freq)
            time.sleep(change_time)
            if step + center_freq > end:
                difference = (step + center_freq) - end
                if reverse:
                    center_freq = end - difference
                    reversing = True
                else:
                    center_freq = start + difference
            elif reversing and center_freq - step < start:
                reversing = False
                center_freq = start + (start - (center_freq - step))
            elif reversing:
                center_freq -= step
            else:
                center_freq += step
