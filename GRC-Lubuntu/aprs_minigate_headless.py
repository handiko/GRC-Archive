#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: APRS I-Gate
# Author: Handiko Gesang - YD1SDL - 2018
# Generated: Wed Apr  4 11:25:02 2018
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from RTL_APRS_RX import RTL_APRS_RX  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import igate


class aprs_minigate_headless(gr.top_block):

    def __init__(self, rfgain=30.0):
        gr.top_block.__init__(self, "APRS I-Gate")

        ##################################################
        # Parameters
        ##################################################
        self.rfgain = rfgain

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1.2e6

        ##################################################
        # Blocks
        ##################################################
        self.igate_aprs_pkt_gen_0_0_1_0_0 = igate.aprs_pkt_gen(3600, 'YD1SDL-10', 'APGRC', 'WIDE2-2', 240, 3, ':BLNA     :New Digi YB2YOU-1 at Mt. Merapi is now in full operational')
        self.igate_aprs_pkt_gen_0_0 = igate.aprs_pkt_gen(180, 'YD1SDL-10', 'APGRC', 'WIDE2-2', 240, 3, '>Automated message generator : OFF')
        self.igate_aprs_pkt_gen_0 = igate.aprs_pkt_gen(180, 'YD1SDL-10', 'APGRC', 'WIDE2-2', 240, 3, '!0745.80S/11022.51E`PHG5130/GNU Radio APRS I-gate - ver 0')
        self.igate_aprs_is_sink_0 = igate.aprs_is_sink('rotate.aprs2.net', 14580, 'YD1SDL-10', 24505)
        self.igate_aprs_demod_0 = igate.aprs_demod(48000)
        self.fft_filter_xxx_3 = filter.fft_filter_fff(1, (firdes.band_pass(1,48e3,1e3,2400,1e2,firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_3.declare_sample_delay(0)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.RTL_APRS_RX_0 = RTL_APRS_RX(
            device_ppm=58,
            freq=144.39e6,
            rf_gain=rfgain,
            samp_rate=samp_rate,
            squelch=-60,
        )

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.igate_aprs_demod_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0_0_1_0_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.connect((self.RTL_APRS_RX_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.RTL_APRS_RX_0, 1), (self.fft_filter_xxx_3, 0))    
        self.connect((self.fft_filter_xxx_3, 0), (self.blocks_null_sink_2, 0))    
        self.connect((self.fft_filter_xxx_3, 0), (self.igate_aprs_demod_0, 0))    

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.RTL_APRS_RX_0.set_rf_gain(self.rfgain)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.RTL_APRS_RX_0.set_samp_rate(self.samp_rate)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-g", "--rfgain", dest="rfgain", type="eng_float", default=eng_notation.num_to_str(30.0),
        help="Set RF Gain (dB) [default=%default]")
    return parser


def main(top_block_cls=aprs_minigate_headless, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(rfgain=options.rfgain)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
