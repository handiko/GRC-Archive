#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Multipath Psk
# Generated: Wed Apr 18 14:47:05 2018
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
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from scipy import fftpack
import numpy
import sip
import sys


class multipath_psk(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multipath Psk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multipath Psk")
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

        self.settings = Qt.QSettings("GNU Radio", "multipath_psk")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tap4 = tap4 = 0.6
        self.tap3 = tap3 = 0.6
        self.tap2 = tap2 = 0.5
        self.tap1 = tap1 = 0.25
        self.taps = taps = fftpack.ifftshift(fftpack.ifft([tap3, tap4, 1.0, tap1, tap2,tap3, tap4, 1.0, tap1, tap2,tap3, tap4, 1.0, tap1, tap2]))
        self.sps = sps = 8
        self.samp_rate = samp_rate = 32000
        
        self.const = const = digital.constellation_16qam().base()
        
        self.cma = cma = -20

        ##################################################
        # Blocks
        ##################################################
        self._tap4_range = Range(0, 1, 0.01, 0.6, 200)
        self._tap4_win = RangeWidget(self._tap4_range, self.set_tap4, "tap4", "slider", float)
        self.top_grid_layout.addWidget(self._tap4_win, 1,3,1,1)
        self._tap3_range = Range(0, 1, 0.01, 0.6, 200)
        self._tap3_win = RangeWidget(self._tap3_range, self.set_tap3, "tap3", "slider", float)
        self.top_grid_layout.addWidget(self._tap3_win, 1,2,1,1)
        self._tap2_range = Range(0, 1, 0.01, 0.5, 200)
        self._tap2_win = RangeWidget(self._tap2_range, self.set_tap2, "tap2", "slider", float)
        self.top_grid_layout.addWidget(self._tap2_win, 1,1,1,1)
        self._tap1_range = Range(0, 1, 0.01, 0.25, 200)
        self._tap1_win = RangeWidget(self._tap1_range, self.set_tap1, "tap1", "slider", float)
        self.top_grid_layout.addWidget(self._tap1_win, 1,0,1,1)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1.0, sps*1.0, 1.0, 0.35, 22*sps))
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, 0)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0,2,1,2)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=const,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(sps*(1+0.0), 0.25*0.01*0.01, 0.5, 0.01, 0.005)
        self._cma_range = Range(-40, -10, 1, -20, 200)
        self._cma_win = RangeWidget(self._cma_range, self.set_cma, "cma", "counter_slider", float)
        self.top_grid_layout.addWidget(self._cma_win, 2,0,1,4)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.01,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.digital_constellation_modulator_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "multipath_psk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tap4(self):
        return self.tap4

    def set_tap4(self, tap4):
        self.tap4 = tap4
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap3(self):
        return self.tap3

    def set_tap3(self, tap3):
        self.tap3 = tap3
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap2(self):
        return self.tap2

    def set_tap2(self, tap2):
        self.tap2 = tap2
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap1(self):
        return self.tap1

    def set_tap1(self, tap1):
        self.tap1 = tap1
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2,self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1.0, self.sps*1.0, 1.0, 0.35, 22*self.sps))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.sps*(1+0.0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const

    def get_cma(self):
        return self.cma

    def set_cma(self, cma):
        self.cma = cma


def main(top_block_cls=multipath_psk, options=None):

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
