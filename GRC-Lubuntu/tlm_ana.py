#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tlm Ana
# Generated: Tue Mar 20 20:11:39 2018
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
import math
import sip
import sys


class tlm_ana(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tlm Ana")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tlm Ana")
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

        self.settings = Qt.QSettings("GNU Radio", "tlm_ana")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 40
        self.nfilt = nfilt = 40
        self.audio_rate = audio_rate = 48e3
        self.samp_rate = samp_rate = 300e3
        
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilt*1.0, audio_rate, 1200.0, 0.35, 16*sps)
          
        self.ch_rate = ch_rate = 96e3

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0 = filter.fir_filter_fff(1, firdes.root_raised_cosine(
        	1.0, audio_rate, 1200.0, 0.35, 16*40))
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(ch_rate),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	8192*8, #size
        	audio_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-15, 15)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 50e-3, 0, 'start')
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
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
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
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.fft_filter_xxx_2 = filter.fft_filter_ccc(1, (firdes.low_pass(1,audio_rate,1e3,1e3,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_2.declare_sample_delay(0)
        self.fft_filter_xxx_1 = filter.fft_filter_fff(1, (firdes.band_pass(1,audio_rate,700,2700,500,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_1.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,5e3,1e3,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0.5, 0.7, 0)
        self.blocks_tagged_file_sink_0 = blocks.tagged_file_sink(gr.sizeof_char*1, int(audio_rate))
        self.blocks_rotator_cc_1 = blocks.rotator_cc((-1700 / audio_rate)*2*math.pi)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(-(-16.2e3 / samp_rate)*2*math.pi)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_5 = blocks.multiply_const_vcc((2, ))
        self.blocks_multiply_const_vxx_4 = blocks.multiply_const_vff((1.0, ))
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((7, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((1e4, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(400, 1.0/400, 4000)
        self.blocks_keep_one_in_n_2 = blocks.keep_one_in_n(gr.sizeof_float*1, 5)
        self.blocks_keep_one_in_n_1 = blocks.keep_one_in_n(gr.sizeof_float*1, 2)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/handiko/gqrx_20180319_072938_433268400_300000_fc.raw', True)
        self.blocks_delay_3 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_short*1, 2400)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_short*1, 400)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 400)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_burst_tagger_1 = blocks.burst_tagger(gr.sizeof_float)
        self.blocks_burst_tagger_1.set_true_tag('burst',True)
        self.blocks_burst_tagger_1.set_false_tag('burst',False)
        	
        self.blocks_burst_tagger_0 = blocks.burst_tagger(gr.sizeof_float)
        self.blocks_burst_tagger_0.set_true_tag('start',True)
        self.blocks_burst_tagger_0.set_false_tag('stop',False)
        	
        self.blocks_add_const_vxx_3 = blocks.add_const_vff((-5, ))
        self.blocks_add_const_vxx_2 = blocks.add_const_vff((5, ))
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((48, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((0, ))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(audio_rate/(2*math.pi*1e3/8.0))
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=int(audio_rate),
        	quad_rate=int(ch_rate),
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.fft_filter_xxx_1, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_burst_tagger_1, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_keep_one_in_n_2, 0))    
        self.connect((self.blocks_add_const_vxx_2, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_add_const_vxx_3, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_burst_tagger_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_burst_tagger_1, 0), (self.blocks_add_const_vxx_1, 0))    
        self.connect((self.blocks_burst_tagger_1, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_delay_1, 0), (self.blocks_burst_tagger_0, 1))    
        self.connect((self.blocks_delay_2, 0), (self.blocks_burst_tagger_1, 1))    
        self.connect((self.blocks_delay_3, 0), (self.blocks_multiply_const_vxx_3, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_rotator_cc_0, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_tagged_file_sink_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_rotator_cc_1, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_delay_1, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_delay_2, 0))    
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.blocks_float_to_short_0, 0))    
        self.connect((self.blocks_keep_one_in_n_2, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_threshold_ff_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_const_vxx_3, 0))    
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.blocks_multiply_const_vxx_5, 0))    
        self.connect((self.blocks_rotator_cc_1, 0), (self.fft_filter_xxx_2, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_keep_one_in_n_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.fft_filter_xxx_1, 0), (self.blocks_burst_tagger_0, 0))    
        self.connect((self.fft_filter_xxx_1, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.fft_filter_xxx_2, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_delay_3, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_multiply_const_vxx_4, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tlm_ana")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_nfilt(self):
        return self.nfilt

    def set_nfilt(self, nfilt):
        self.nfilt = nfilt

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1.0, self.audio_rate, 1200.0, 0.35, 16*40))
        self.qtgui_time_sink_x_0.set_samp_rate(self.audio_rate)
        self.fft_filter_xxx_2.set_taps((firdes.low_pass(1,self.audio_rate,1e3,1e3,firdes.WIN_BLACKMAN)))
        self.fft_filter_xxx_1.set_taps((firdes.band_pass(1,self.audio_rate,700,2700,500,firdes.WIN_BLACKMAN)))
        self.blocks_rotator_cc_1.set_phase_inc((-1700 / self.audio_rate)*2*math.pi)
        self.analog_quadrature_demod_cf_0.set_gain(self.audio_rate/(2*math.pi*1e3/8.0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.fft_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,5e3,1e3,firdes.WIN_BLACKMAN)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_rotator_cc_0.set_phase_inc(-(-16.2e3 / self.samp_rate)*2*math.pi)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_ch_rate(self):
        return self.ch_rate

    def set_ch_rate(self, ch_rate):
        self.ch_rate = ch_rate


def main(top_block_cls=tlm_ana, options=None):

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
