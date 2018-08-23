#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: TLM RTL RX
# Generated: Fri Apr 20 07:32:50 2018
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
from carrier_detect import carrier_detect  # grc-generated hier_block
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
from optparse import OptionParser
import display
import handiko
import math
import sip


class tlm_rtl(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TLM RTL RX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TLM RTL RX")
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

        self.settings = Qt.QSettings("GNU Radio", "tlm_rtl")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 40
        self.samp_rate = samp_rate = 300e3
        self.nfilt = nfilt = 40
        self.gain_mu = gain_mu = 0.5
        self.ch_rate = ch_rate = 96e3
        self.cfreq = cfreq = 144.12
        self.audio_rate = audio_rate = 48e3

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'RF Spectrum')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'RF Spectrogram')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Demod')
        self.top_grid_layout.addWidget(self.tab, 0,0,1,1)
        self._cfreq_tool_bar = Qt.QToolBar(self)
        self._cfreq_tool_bar.addWidget(Qt.QLabel('Center Freq. (MHz)'+": "))
        self._cfreq_line_edit = Qt.QLineEdit(str(self.cfreq))
        self._cfreq_tool_bar.addWidget(self._cfreq_line_edit)
        self._cfreq_line_edit.returnPressed.connect(
        	lambda: self.set_cfreq(eng_notation.str_to_num(str(self._cfreq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._cfreq_tool_bar, 2,0,1,1)
        self.show_text_0 = display.show_text()
        self._show_text_0_win = sip.wrapinstance(self.show_text_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._show_text_0_win, 1,0,1,1)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=8,
                decimation=40,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(audio_rate),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	cfreq*1e6, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
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
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, -20)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	8192*2, #size
        	1200*8, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-15, 15)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 200e-3, 0, 'start')
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "blue", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
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
        self.tab_layout_2.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	cfreq*1e6, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-120, 0)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_freq_sink_x_1_win)
        self.handiko_parse_frame_0 = handiko.parse_frame()
        self.handiko_frame_detect_0 = handiko.frame_detect()
        self.fsk_demod_1 = fsk_demod(
            baud=1200,
            fsk_hi_tone=2200,
            fsk_lo_tone=1200,
            in_sps=40,
            out_sps=8,
        )
        self.fsk_demod_0 = fsk_demod(
            baud=1200,
            fsk_hi_tone=2200,
            fsk_lo_tone=1200,
            in_sps=sps,
            out_sps=2,
        )
        self.digital_clock_recovery_mm_xx_0_0 = digital.clock_recovery_mm_ff(2*(1+0.0), 0.25*gain_mu*gain_mu, 0.5, gain_mu, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.carrier_detect_0 = carrier_detect(
            hi=0.7,
            low=0.5,
            gain=10e3,
            filter_len=400,
        )
        self.blocks_throttle_2 = blocks.throttle(gr.sizeof_float*1, 1200*8,True)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, 1200*8,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '', '52001', 10000, False)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(0)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_multiply_const_vxx_5 = blocks.multiply_const_vcc((2, ))
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vff((4, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((7, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/handiko/gqrx_20180404_011711_144119900_300000_fc.raw', True)
        self.blocks_delay_3 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_burst_tagger_0 = blocks.burst_tagger(gr.sizeof_float)
        self.blocks_burst_tagger_0.set_true_tag('start',True)
        self.blocks_burst_tagger_0.set_false_tag('stop',False)
        	
        self.blocks_add_const_vxx_3 = blocks.add_const_vff((-5, ))
        self.blocks_add_const_vxx_2 = blocks.add_const_vff((5, ))
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=int(audio_rate),
        	quad_rate=int(audio_rate),
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.handiko_frame_detect_0, 'frame out'), (self.handiko_parse_frame_0, 'frame in'))    
        self.msg_connect((self.handiko_parse_frame_0, 'info out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.msg_connect((self.handiko_parse_frame_0, 'info out'), (self.blocks_socket_pdu_0, 'pdus'))    
        self.connect((self.analog_nbfm_rx_0, 0), (self.blocks_burst_tagger_0, 0))    
        self.connect((self.analog_nbfm_rx_0, 0), (self.fsk_demod_0, 0))    
        self.connect((self.analog_nbfm_rx_0, 0), (self.fsk_demod_1, 0))    
        self.connect((self.blocks_add_const_vxx_2, 0), (self.blocks_throttle_2, 0))    
        self.connect((self.blocks_add_const_vxx_3, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.blocks_burst_tagger_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_delay_3, 0), (self.blocks_multiply_const_vxx_3, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_rotator_cc_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_const_vxx_3, 0))    
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.show_text_0, 0))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.blocks_multiply_const_vxx_5, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_throttle_2, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.carrier_detect_0, 0), (self.blocks_burst_tagger_0, 1))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.handiko_frame_detect_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.fsk_demod_0, 0), (self.digital_clock_recovery_mm_xx_0_0, 0))    
        self.connect((self.fsk_demod_1, 0), (self.blocks_delay_3, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.carrier_detect_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_delay_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tlm_rtl")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.fsk_demod_0.set_in_sps(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.cfreq*1e6, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.cfreq*1e6, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_nfilt(self):
        return self.nfilt

    def set_nfilt(self, nfilt):
        self.nfilt = nfilt

    def get_gain_mu(self):
        return self.gain_mu

    def set_gain_mu(self, gain_mu):
        self.gain_mu = gain_mu
        self.digital_clock_recovery_mm_xx_0_0.set_gain_omega(0.25*self.gain_mu*self.gain_mu)
        self.digital_clock_recovery_mm_xx_0_0.set_gain_mu(self.gain_mu)

    def get_ch_rate(self):
        return self.ch_rate

    def set_ch_rate(self, ch_rate):
        self.ch_rate = ch_rate

    def get_cfreq(self):
        return self.cfreq

    def set_cfreq(self, cfreq):
        self.cfreq = cfreq
        Qt.QMetaObject.invokeMethod(self._cfreq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.cfreq)))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.cfreq*1e6, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.cfreq*1e6, self.samp_rate)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate


def main(top_block_cls=tlm_rtl, options=None):

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
