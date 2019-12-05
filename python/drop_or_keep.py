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

class drop_or_keep(gr.sync_block):
    """
    docstring for block drop_or_keep
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="drop_or_keep",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])
        self.drop = False
        self.message_port_register_in(pmt.intern("commands"))
        self.set_msg_handler(pmt.intern("commands"), self.receive_message)

    def receive_message(self, message):
        self.drop = pmt.to_bool(pmt.cdr(message))

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        temp = in0
        if self.drop:
            # for i in range(len(temp)):
            #     temp[i] = 0
            temp = []
        out[:] = temp
        return len(output_items[0])
