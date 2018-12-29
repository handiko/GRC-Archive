#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: APRS I-Gate
# Author: Handiko Gesang - YD1SDL - 2018
# Generated: Sat Dec 29 01:12:48 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import igate
import sys


class aprs_minigate(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "APRS I-Gate")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("APRS I-Gate")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "aprs_minigate")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1.2e6
        self.rfgain = rfgain = 30

        ##################################################
        # Blocks
        ##################################################
        self._rfgain_range = Range(0, 49, 1, 30, 200)
        self._rfgain_win = RangeWidget(self._rfgain_range, self.set_rfgain, 'RF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rfgain_win, 1,0,1,2)
        self.igate_debug_print_msg_0 = igate.debug_print_msg()
        self.igate_aprs_pkt_gen_0_0 = igate.aprs_pkt_gen(300, 'YD1SDL-10', 'APGRC', 'WIDE2-2', 240, 3, '>Non Permanent - Experimental')
        self.igate_aprs_pkt_gen_0 = igate.aprs_pkt_gen(120, 'YD1SDL-10', 'APGRC', 'WIDE2-2', 240, 3, '!0615.52S/10643.56E`PHG5130/GNU Radio APRS I-gate - ver 0')
        self.igate_aprs_is_sink_0 = igate.aprs_is_sink('rotate.aprs.net', 14580, 'YD1SDL-10', 24505)
        self.igate_aprs_demod_0 = igate.aprs_demod(48000)
        self.fft_filter_xxx_3 = filter.fft_filter_fff(1, (firdes.band_pass(10,48e3,1e3,2400,1e2,firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_3.declare_sample_delay(0)
        self.audio_source_0 = audio.source(48000, '', True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.igate_aprs_demod_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.msg_connect((self.igate_aprs_demod_0, 'out'), (self.igate_debug_print_msg_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0, 'out'), (self.igate_debug_print_msg_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0_0, 'out'), (self.igate_debug_print_msg_0, 'in'))    
        self.connect((self.audio_source_0, 0), (self.fft_filter_xxx_3, 0))    
        self.connect((self.fft_filter_xxx_3, 0), (self.igate_aprs_demod_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "aprs_minigate")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain


def main(top_block_cls=aprs_minigate, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
