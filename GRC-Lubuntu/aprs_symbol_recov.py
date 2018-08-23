#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: APRS Symbol Recovery
# Author: Handiko Gesang - YD1SDL - 2018
# Generated: Tue Apr 17 17:56:23 2018
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

from PyQt4 import Qt
from fsk_demod import fsk_demod  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import afsk
import display
import hdlc_to_ax25
import math
import osmosdr
import packet  # embedded python module
import sip
import time


class aprs_symbol_recov(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "APRS Symbol Recovery")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("APRS Symbol Recovery")
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

        self.settings = Qt.QSettings("GNU Radio", "aprs_symbol_recov")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.ch_rate = ch_rate = 48e3
        self.bb_rate = bb_rate = 192e3
        self.afsk_spec = afsk_spec = [1200, 1200, 2200]
        self.thresh = thresh = -50*2
        self.samp_rate = samp_rate = 2.88e6
        self.rfgain = rfgain = 10
        self.out_sps = out_sps = 2
        self.in_sps = in_sps = int(ch_rate) / afsk_spec[0]
        self.gain_mu = gain_mu = 0.175
        self.freq = freq = 144.39e6
        self.dev_ppm = dev_ppm = 52
        self.bb_decim = bb_decim = int(bb_rate)/int(ch_rate)
        self.afgain = afgain = -7

        ##################################################
        # Blocks
        ##################################################
        self._rfgain_range = Range(0, 49, 1, 10, 100)
        self._rfgain_win = RangeWidget(self._rfgain_range, self.set_rfgain, 'RF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rfgain_win, 3,0,1,1)
        self.show_text_2 = display.show_text()
        self._show_text_2_win = sip.wrapinstance(self.show_text_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._show_text_2_win, 2,2,2,1)
        self.show_text_0 = display.show_text()
        self._show_text_0_win = sip.wrapinstance(self.show_text_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._show_text_0_win, 2,0,1,2)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	192e3, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(False)
        
        if not False:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [6, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-105, -20)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0,2,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	1200, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-4.2, 4.2)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1,0,1,3)
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
        colors = ["blue", "red", "green", "black", "cyan",
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.pfb_decimator_ccf_0_0 = pfb.decimator_ccf(
        	  int(samp_rate / ch_rate),
        	  (),
        	  0,
        	  100,
                  True,
                  True)
        self.pfb_decimator_ccf_0_0.declare_sample_delay(0)
        	
        self.pfb_decimator_ccf_0 = pfb.decimator_ccf(
        	  int(samp_rate / bb_rate),
        	  (),
        	  0,
        	  100,
                  True,
                  True)
        self.pfb_decimator_ccf_0.declare_sample_delay(0)
        	
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(dev_ppm, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rfgain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.hdlc_to_ax25 = hdlc_to_ax25.blk()
        self.fsk_demod_0 = fsk_demod(
            baud=afsk_spec[0],
            fsk_hi_tone=afsk_spec[2],
            fsk_lo_tone=afsk_spec[1],
            in_sps=in_sps,
            out_sps=out_sps,
        )
        self.fft_filter_xxx_1 = filter.fft_filter_fff(1, (firdes.band_pass(1,ch_rate,400,5e3,400,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_1.declare_sample_delay(0)
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(32, 500)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(out_sps*(1+0.0), 0.25*gain_mu*gain_mu, 0.5, gain_mu, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '', '52001', 10000, False)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_not_xx_0 = blocks.not_bb()
        self.blocks_and_const_xx_0 = blocks.and_const_bb(1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(ch_rate/(2*math.pi*12e3/8.0))
        self.afsk_afsk1200_0 = afsk.afsk1200(int(ch_rate),4)
        self._afgain_range = Range(-20, -1, 0.1, -7, 100)
        self._afgain_win = RangeWidget(self._afgain_range, self.set_afgain, 'AF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._afgain_win, 3,1,1,1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.hdlc_to_ax25, 'hdlc in'))    
        self.msg_connect((self.hdlc_to_ax25, 'ax25 out'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))    
        self.msg_connect((self.hdlc_to_ax25, 'ax25 out'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.afsk_afsk1200_0, 0), (self.show_text_2, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.fft_filter_xxx_1, 0))    
        self.connect((self.blocks_and_const_xx_0, 0), (self.digital_hdlc_deframer_bp_0, 0))    
        self.connect((self.blocks_not_xx_0, 0), (self.blocks_and_const_xx_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.show_text_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_not_xx_0, 0))    
        self.connect((self.fft_filter_xxx_1, 0), (self.afsk_afsk1200_0, 0))    
        self.connect((self.fft_filter_xxx_1, 0), (self.fsk_demod_0, 0))    
        self.connect((self.fsk_demod_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.pfb_decimator_ccf_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.pfb_decimator_ccf_0_0, 0))    
        self.connect((self.pfb_decimator_ccf_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.pfb_decimator_ccf_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.pfb_decimator_ccf_0_0, 0), (self.analog_quadrature_demod_cf_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "aprs_symbol_recov")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_ch_rate(self):
        return self.ch_rate

    def set_ch_rate(self, ch_rate):
        self.ch_rate = ch_rate
        self.set_in_sps(int(self.ch_rate) / self.afsk_spec[0])
        self.fft_filter_xxx_1.set_taps((firdes.band_pass(1,self.ch_rate,400,5e3,400,firdes.WIN_BLACKMAN)))
        self.set_bb_decim(int(self.bb_rate)/int(self.ch_rate))
        self.analog_quadrature_demod_cf_0.set_gain(self.ch_rate/(2*math.pi*12e3/8.0))

    def get_bb_rate(self):
        return self.bb_rate

    def set_bb_rate(self, bb_rate):
        self.bb_rate = bb_rate
        self.set_bb_decim(int(self.bb_rate)/int(self.ch_rate))

    def get_afsk_spec(self):
        return self.afsk_spec

    def set_afsk_spec(self, afsk_spec):
        self.afsk_spec = afsk_spec
        self.set_in_sps(int(self.ch_rate) / self.afsk_spec[0])
        self.fsk_demod_0.set_baud(self.afsk_spec[0])
        self.fsk_demod_0.set_fsk_hi_tone(self.afsk_spec[2])
        self.fsk_demod_0.set_fsk_lo_tone(self.afsk_spec[1])

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.osmosdr_source_0.set_gain(self.rfgain, 0)

    def get_out_sps(self):
        return self.out_sps

    def set_out_sps(self, out_sps):
        self.out_sps = out_sps
        self.fsk_demod_0.set_out_sps(self.out_sps)
        self.digital_clock_recovery_mm_xx_0.set_omega(self.out_sps*(1+0.0))

    def get_in_sps(self):
        return self.in_sps

    def set_in_sps(self, in_sps):
        self.in_sps = in_sps
        self.fsk_demod_0.set_in_sps(self.in_sps)

    def get_gain_mu(self):
        return self.gain_mu

    def set_gain_mu(self, gain_mu):
        self.gain_mu = gain_mu
        self.digital_clock_recovery_mm_xx_0.set_gain_omega(0.25*self.gain_mu*self.gain_mu)
        self.digital_clock_recovery_mm_xx_0.set_gain_mu(self.gain_mu)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_dev_ppm(self):
        return self.dev_ppm

    def set_dev_ppm(self, dev_ppm):
        self.dev_ppm = dev_ppm
        self.osmosdr_source_0.set_freq_corr(self.dev_ppm, 0)

    def get_bb_decim(self):
        return self.bb_decim

    def set_bb_decim(self, bb_decim):
        self.bb_decim = bb_decim

    def get_afgain(self):
        return self.afgain

    def set_afgain(self, afgain):
        self.afgain = afgain


def main(top_block_cls=aprs_symbol_recov, options=None):

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
