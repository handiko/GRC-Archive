#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Merapi Vco Demo
# Generated: Tue Mar 27 04:52:26 2018
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import osmosdr
import sip
import sys
import time


class merapi_vco_demo(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Merapi Vco Demo")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Merapi Vco Demo")
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

        self.settings = Qt.QSettings("GNU Radio", "merapi_vco_demo")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.4e6
        self.rfgain = rfgain = 30
        self.ch_rate = ch_rate = 48e3
        self.cfreq = cfreq = 165807500
        self.bb_rate = bb_rate = 192e3
        self.audio_mute = audio_mute = False
        self.afgain = afgain = -20

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Input Spectrum')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Baseband')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Demodulated Audio')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'Sensor - Voltage')
        self.tab_widget_4 = Qt.QWidget()
        self.tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_4)
        self.tab_grid_layout_4 = Qt.QGridLayout()
        self.tab_layout_4.addLayout(self.tab_grid_layout_4)
        self.tab.addTab(self.tab_widget_4, 'Sensor - Freq')
        self.tab_widget_5 = Qt.QWidget()
        self.tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_5)
        self.tab_grid_layout_5 = Qt.QGridLayout()
        self.tab_layout_5.addLayout(self.tab_grid_layout_5)
        self.tab.addTab(self.tab_widget_5, 'Tab 5')
        self.tab_widget_6 = Qt.QWidget()
        self.tab_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_6)
        self.tab_grid_layout_6 = Qt.QGridLayout()
        self.tab_layout_6.addLayout(self.tab_grid_layout_6)
        self.tab.addTab(self.tab_widget_6, 'Tab 6')
        self.tab_widget_7 = Qt.QWidget()
        self.tab_layout_7 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_7)
        self.tab_grid_layout_7 = Qt.QGridLayout()
        self.tab_layout_7.addLayout(self.tab_grid_layout_7)
        self.tab.addTab(self.tab_widget_7, 'Tab 7')
        self.tab_widget_8 = Qt.QWidget()
        self.tab_layout_8 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_8)
        self.tab_grid_layout_8 = Qt.QGridLayout()
        self.tab_layout_8.addLayout(self.tab_grid_layout_8)
        self.tab.addTab(self.tab_widget_8, 'Tab 8')
        self.tab_widget_9 = Qt.QWidget()
        self.tab_layout_9 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_9)
        self.tab_grid_layout_9 = Qt.QGridLayout()
        self.tab_layout_9.addLayout(self.tab_grid_layout_9)
        self.tab.addTab(self.tab_widget_9, 'Tab 9')
        self.top_layout.addWidget(self.tab)
        self._rfgain_range = Range(0, 50, 1, 30, 200)
        self._rfgain_win = RangeWidget(self._rfgain_range, self.set_rfgain, 'RF Gain (dB)', "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._rfgain_win, 1,1,1,1)
        self._cfreq_tool_bar = Qt.QToolBar(self)
        self._cfreq_tool_bar.addWidget(Qt.QLabel('Freq. (Hz)'+": "))
        self._cfreq_line_edit = Qt.QLineEdit(str(self.cfreq))
        self._cfreq_tool_bar.addWidget(self._cfreq_line_edit)
        self._cfreq_line_edit.returnPressed.connect(
        	lambda: self.set_cfreq(int(str(self._cfreq_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._cfreq_tool_bar, 1,0,1,1)
        _audio_mute_check_box = Qt.QCheckBox('Audio Mute')
        self._audio_mute_choices = {True: True, False: False}
        self._audio_mute_choices_inv = dict((v,k) for k,v in self._audio_mute_choices.iteritems())
        self._audio_mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_audio_mute_check_box, "setChecked", Qt.Q_ARG("bool", self._audio_mute_choices_inv[i]))
        self._audio_mute_callback(self.audio_mute)
        _audio_mute_check_box.stateChanged.connect(lambda i: self.set_audio_mute(self._audio_mute_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_audio_mute_check_box, 2,0,1,1)
        self._afgain_range = Range(-30, -1, 1, -20, 200)
        self._afgain_win = RangeWidget(self._afgain_range, self.set_afgain, 'AF Gain (dB)', "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._afgain_win, 2,1,1,1)
        self.rational_resampler_xxx_2 = filter.rational_resampler_fff(
                interpolation=5,
                decimation=48,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=10,
                decimation=48,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(bb_rate),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_f(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	5e3, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.01)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
        if not False:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not False)
        
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
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-50, 0)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_4.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	8192*8, #size
        	ch_rate/10, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-8, 8)
        
        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(True)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        
        if not False:
          self.qtgui_time_sink_x_2.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_2_win, 1,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	2048, #size
        	ch_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-15, 15)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
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
        self.tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win, 0,0,1,1)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_f(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	10e3, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_2.set_y_axis(-50, 0)
        self.qtgui_freq_sink_x_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(False)
        self.qtgui_freq_sink_x_2.enable_grid(True)
        self.qtgui_freq_sink_x_2.set_fft_average(0.1)
        self.qtgui_freq_sink_x_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_2.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_2.set_plot_pos_half(not False)
        
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
                self.qtgui_freq_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_2.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_2_win, 0,1,1,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	bb_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-100, -20)
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
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_1_win, 0,0,1,1)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(cfreq + samp_rate/4, 0)
        self.osmosdr_source_0.set_freq_corr(55, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rfgain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.fft_filter_xxx_4 = filter.fft_filter_fff(1, (firdes.low_pass(1,ch_rate,5000,1000,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_4.declare_sample_delay(0)
        self.fft_filter_xxx_2 = filter.fft_filter_fff(1, (firdes.band_pass(1,ch_rate,600,2000,600,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_2.declare_sample_delay(0)
        self.fft_filter_xxx_1_0 = filter.fft_filter_fff(10, (firdes.low_pass(1,48000,40,40,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_1_0.declare_sample_delay(0)
        self.fft_filter_xxx_1 = filter.fft_filter_ccc(int(bb_rate / ch_rate), (firdes.low_pass(1,bb_rate,ch_rate/2,ch_rate/10,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_1.declare_sample_delay(0)
        self.fft_filter_xxx_0_0 = filter.fft_filter_ccc(1, (firdes.low_pass(1,48000,700,200,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.low_pass(1,samp_rate,bb_rate/2,bb_rate/10,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_rotator_cc_0_0 = blocks.rotator_cc((-1360 / 48000.0) *2*math.pi)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(math.pi / 2)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((pow(10,afgain/10), ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blks2_valve_0 = grc_blks2.valve(item_size=gr.sizeof_float*1, open=bool(audio_mute))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf(ch_rate/(2*math.pi*1000/8.0))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(ch_rate /(2*math.pi*12500/8.0))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.fft_filter_xxx_2, 0))    
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.fft_filter_xxx_1_0, 0))    
        self.connect((self.blks2_valve_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_rotator_cc_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.blocks_rotator_cc_0_0, 0), (self.fft_filter_xxx_0_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.fft_filter_xxx_0_0, 0), (self.analog_quadrature_demod_cf_1, 0))    
        self.connect((self.fft_filter_xxx_1, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.fft_filter_xxx_1_0, 0), (self.qtgui_time_sink_x_2, 0))    
        self.connect((self.fft_filter_xxx_2, 0), (self.blks2_valve_0, 0))    
        self.connect((self.fft_filter_xxx_2, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.fft_filter_xxx_2, 0), (self.fft_filter_xxx_4, 0))    
        self.connect((self.fft_filter_xxx_2, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.fft_filter_xxx_2, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.fft_filter_xxx_4, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_rotator_cc_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.fft_filter_xxx_1, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_freq_sink_x_2, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_waterfall_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "merapi_vco_demo")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_center_freq(self.cfreq + self.samp_rate/4, 0)
        self.fft_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.bb_rate/2,self.bb_rate/10,firdes.WIN_BLACKMAN)))

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.osmosdr_source_0.set_gain(self.rfgain, 0)

    def get_ch_rate(self):
        return self.ch_rate

    def set_ch_rate(self, ch_rate):
        self.ch_rate = ch_rate
        self.qtgui_time_sink_x_2.set_samp_rate(self.ch_rate/10)
        self.qtgui_time_sink_x_0.set_samp_rate(self.ch_rate)
        self.fft_filter_xxx_4.set_taps((firdes.low_pass(1,self.ch_rate,5000,1000,firdes.WIN_BLACKMAN)))
        self.fft_filter_xxx_2.set_taps((firdes.band_pass(1,self.ch_rate,600,2000,600,firdes.WIN_BLACKMAN)))
        self.fft_filter_xxx_1.set_taps((firdes.low_pass(1,self.bb_rate,self.ch_rate/2,self.ch_rate/10,firdes.WIN_BLACKMAN)))
        self.analog_quadrature_demod_cf_1.set_gain(self.ch_rate/(2*math.pi*1000/8.0))
        self.analog_quadrature_demod_cf_0.set_gain(self.ch_rate /(2*math.pi*12500/8.0))

    def get_cfreq(self):
        return self.cfreq

    def set_cfreq(self, cfreq):
        self.cfreq = cfreq
        Qt.QMetaObject.invokeMethod(self._cfreq_line_edit, "setText", Qt.Q_ARG("QString", str(self.cfreq)))
        self.osmosdr_source_0.set_center_freq(self.cfreq + self.samp_rate/4, 0)

    def get_bb_rate(self):
        return self.bb_rate

    def set_bb_rate(self, bb_rate):
        self.bb_rate = bb_rate
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.bb_rate)
        self.fft_filter_xxx_1.set_taps((firdes.low_pass(1,self.bb_rate,self.ch_rate/2,self.ch_rate/10,firdes.WIN_BLACKMAN)))
        self.fft_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.bb_rate/2,self.bb_rate/10,firdes.WIN_BLACKMAN)))

    def get_audio_mute(self):
        return self.audio_mute

    def set_audio_mute(self, audio_mute):
        self.audio_mute = audio_mute
        self._audio_mute_callback(self.audio_mute)
        self.blks2_valve_0.set_open(bool(self.audio_mute))

    def get_afgain(self):
        return self.afgain

    def set_afgain(self, afgain):
        self.afgain = afgain
        self.blocks_multiply_const_vxx_0.set_k((pow(10,self.afgain/10), ))


def main(top_block_cls=merapi_vco_demo, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

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
