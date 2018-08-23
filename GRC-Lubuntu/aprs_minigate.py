#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: APRS I-Gate
# Author: Handiko Gesang - YD1SDL - 2018
# Generated: Sat Mar 31 20:36:13 2018
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from DL1KSV_AFSK_1200baud_demod import DL1KSV_AFSK_1200baud_demod  # grc-generated hier_block
from PyQt4 import Qt
from RTL_APRS_RX import RTL_APRS_RX  # grc-generated hier_block
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import afsk
import display
import sip


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
        self.show_text_0 = display.show_text()
        self._show_text_0_win = sip.wrapinstance(self.show_text_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._show_text_0_win, 2,0,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	144.39e6, #fc
        	192e3, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(False)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [0.8, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.fft_filter_xxx_3 = filter.fft_filter_fff(1, (firdes.band_pass(1,48e3,1e3,2400,1e2,firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_3.declare_sample_delay(0)
        self.afsk_aprs2inet_1 = afsk.aprs2inet(48000, 4)
        self.RTL_APRS_RX_0 = RTL_APRS_RX(
            device_ppm=58,
            freq=144.39e6,
            rf_gain=rfgain,
            samp_rate=samp_rate,
        )
        self.DL1KSV_AFSK_1200baud_demod_0 = DL1KSV_AFSK_1200baud_demod(
            samp_rate=48000,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.DL1KSV_AFSK_1200baud_demod_0, 0), (self.afsk_aprs2inet_1, 0))    
        self.connect((self.RTL_APRS_RX_0, 1), (self.fft_filter_xxx_3, 0))    
        self.connect((self.RTL_APRS_RX_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.afsk_aprs2inet_1, 0), (self.show_text_0, 0))    
        self.connect((self.fft_filter_xxx_3, 0), (self.DL1KSV_AFSK_1200baud_demod_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "aprs_minigate")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.RTL_APRS_RX_0.set_samp_rate(self.samp_rate)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.RTL_APRS_RX_0.set_rf_gain(self.rfgain)


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
