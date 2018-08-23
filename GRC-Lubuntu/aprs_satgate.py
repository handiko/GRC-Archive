#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: APRS S-Gate
# Author: Handiko Gesang - YD1SDL - 2018
# Generated: Fri Mar 23 08:12:12 2018
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
from RTL_APRS_RX import RTL_APRS_RX  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
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
import gpredict
import igate
import math
import sip


class aprs_satgate(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "APRS S-Gate")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("APRS S-Gate")
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

        self.settings = Qt.QSettings("GNU Radio", "aprs_satgate")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.freq = freq = 145.825e6
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = int(freq)
        self.samp_rate = samp_rate = 2.4e6
        
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(4, 48000, 1200, 0.35, 16*48000/1200)
          
        self.rfgain = rfgain = 35
        self.audio_mute = audio_mute = True
        self.afgain = afgain = -7

        ##################################################
        # Blocks
        ##################################################
        self._rfgain_range = Range(0, 49, 1, 35, 200)
        self._rfgain_win = RangeWidget(self._rfgain_range, self.set_rfgain, 'RF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rfgain_win, 3,0,1,1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: x
        
        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Freq (Hz)'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 4,0,1,1)
          
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
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	2048, #size
        	1200, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-4, 4)
        
        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(True)
        self.qtgui_time_sink_x_2.enable_axis_labels(False)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        
        if not False:
          self.qtgui_time_sink_x_2.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "blue", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [0.7, 0.7, 1.0, 1.0, 1.0,
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_win, 1,0,1,3)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.igate_aprs_pkt_gen_0 = igate.aprs_pkt_gen(120, 'YD1SDL-10', 'APGRC', 'WIDE2-2', 240, 3, '!0745.80S/11022.51E` Temporary / Experimental APRS I/S-Gate')
        self.igate_aprs_is_sink_0 = igate.aprs_is_sink('rotate.aprs.net', 14580, 'YD1SDL-10', 24505)
        self.igate_aprs_demod_0 = igate.aprs_demod(48000)
        self.gpredict_doppler_0 = gpredict.doppler(self.set_freq, "localhost", 4532, True)
        self.fft_filter_xxx_3 = filter.fft_filter_fff(1, (firdes.band_pass(0.5,48e3,1e3,2400,1e2,firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_3.declare_sample_delay(0)
        self.fft_filter_xxx_2 = filter.fft_filter_fff(2, (firdes.band_pass(0.25,48e3,400,2500,500,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_2.declare_sample_delay(0)
        self.fft_filter_xxx_1 = filter.fft_filter_fff(1, (rrc_taps), 1)
        self.fft_filter_xxx_1.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.low_pass(1,48e3,1e3,1e2,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_fff(48000 / 1200, 6.28 / 1000, (rrc_taps), 39, 20, 1.5, 1)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('IO86-wav-dump.wav', 1, 24000, 16)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(-1700 / 48e3 * 2 * math.pi)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, 10)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(10e3*math.pi), 1.0/(10e3*math.pi), 4000)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        _audio_mute_check_box = Qt.QCheckBox('Audio Mute')
        self._audio_mute_choices = {True: True, False: False}
        self._audio_mute_choices_inv = dict((v,k) for k,v in self._audio_mute_choices.iteritems())
        self._audio_mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_audio_mute_check_box, "setChecked", Qt.Q_ARG("bool", self._audio_mute_choices_inv[i]))
        self._audio_mute_callback(self.audio_mute)
        _audio_mute_check_box.stateChanged.connect(lambda i: self.set_audio_mute(self._audio_mute_choices[bool(i)]))
        self.top_grid_layout.addWidget(_audio_mute_check_box, 4,1,1,1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(48e3 / (2*math.pi*1200/8.0))
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-1, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self.afsk_aprs2inet_1 = afsk.aprs2inet(12000, 4)
        self.afsk_afsk1200_0 = afsk.afsk1200(48000,4)
        self._afgain_range = Range(-20, -1, 0.1, -7, 200)
        self._afgain_win = RangeWidget(self._afgain_range, self.set_afgain, 'AF Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._afgain_win, 3,1,1,1)
        self.RTL_APRS_RX_0 = RTL_APRS_RX(
            device_ppm=58,
            freq=freq,
            rf_gain=rfgain,
            samp_rate=samp_rate,
        )

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.igate_aprs_demod_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.msg_connect((self.igate_aprs_pkt_gen_0, 'out'), (self.igate_aprs_is_sink_0, 'in'))    
        self.connect((self.RTL_APRS_RX_0, 1), (self.fft_filter_xxx_2, 0))    
        self.connect((self.RTL_APRS_RX_0, 1), (self.fft_filter_xxx_3, 0))    
        self.connect((self.RTL_APRS_RX_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.RTL_APRS_RX_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.afsk_afsk1200_0, 0), (self.show_text_2, 0))    
        self.connect((self.afsk_aprs2inet_1, 0), (self.show_text_0, 0))    
        self.connect((self.analog_agc2_xx_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_rotator_cc_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_repeat_0, 0), (self.afsk_aprs2inet_1, 0))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.fft_filter_xxx_1, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_time_sink_x_2, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.fft_filter_xxx_1, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.fft_filter_xxx_2, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.fft_filter_xxx_3, 0), (self.afsk_afsk1200_0, 0))    
        self.connect((self.fft_filter_xxx_3, 0), (self.blocks_float_to_complex_0_0, 0))    
        self.connect((self.fft_filter_xxx_3, 0), (self.igate_aprs_demod_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "aprs_satgate")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(int(self.freq)))
        self.RTL_APRS_RX_0.set_freq(self.freq)

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_0)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.RTL_APRS_RX_0.set_samp_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.fft_filter_xxx_1.set_taps((self.rrc_taps))
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.RTL_APRS_RX_0.set_rf_gain(self.rfgain)

    def get_audio_mute(self):
        return self.audio_mute

    def set_audio_mute(self, audio_mute):
        self.audio_mute = audio_mute
        self._audio_mute_callback(self.audio_mute)

    def get_afgain(self):
        return self.afgain

    def set_afgain(self, afgain):
        self.afgain = afgain


def main(top_block_cls=aprs_satgate, options=None):

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
