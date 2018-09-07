#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Bcfm Channelizer
# Generated: Wed Aug 29 19:23:15 2018
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class bcfm_channelizer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Bcfm Channelizer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Bcfm Channelizer")
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

        self.settings = Qt.QSettings("GNU Radio", "bcfm_channelizer")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.8e6
        self.disp_min = disp_min = -100
        self.disp_max = disp_max = -10

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'RF In')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Channels')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Tab 2')
        self.top_layout.addWidget(self.tab)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
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
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-90, 0)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_6 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_6.set_update_time(0.10)
        self.qtgui_freq_sink_x_6.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_6.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_6.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_6.enable_autoscale(False)
        self.qtgui_freq_sink_x_6.enable_grid(False)
        self.qtgui_freq_sink_x_6.set_fft_average(1.0)
        self.qtgui_freq_sink_x_6.enable_axis_labels(True)
        self.qtgui_freq_sink_x_6.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_6.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_6.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_6.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_6.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_6.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_6.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_6.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_6_win = sip.wrapinstance(self.qtgui_freq_sink_x_6.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_6_win, 2,0,1,1)
        self.qtgui_freq_sink_x_5 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_5.set_update_time(0.10)
        self.qtgui_freq_sink_x_5.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_5.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_5.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_5.enable_autoscale(False)
        self.qtgui_freq_sink_x_5.enable_grid(False)
        self.qtgui_freq_sink_x_5.set_fft_average(1.0)
        self.qtgui_freq_sink_x_5.enable_axis_labels(True)
        self.qtgui_freq_sink_x_5.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_5.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_5.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_5.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_5.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_5.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_5.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_5.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_5_win = sip.wrapinstance(self.qtgui_freq_sink_x_5.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_5_win, 1,2,1,1)
        self.qtgui_freq_sink_x_4 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_4.set_update_time(0.10)
        self.qtgui_freq_sink_x_4.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_4.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_4.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_4.enable_autoscale(False)
        self.qtgui_freq_sink_x_4.enable_grid(False)
        self.qtgui_freq_sink_x_4.set_fft_average(1.0)
        self.qtgui_freq_sink_x_4.enable_axis_labels(True)
        self.qtgui_freq_sink_x_4.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_4.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_4.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_4.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_4.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_4.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_4.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_4.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_4_win = sip.wrapinstance(self.qtgui_freq_sink_x_4.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_4_win, 1,1,1,1)
        self.qtgui_freq_sink_x_3_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_3_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_3_0.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_3_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_3_0.enable_grid(True)
        self.qtgui_freq_sink_x_3_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_3_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_3_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_3_0.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_3_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_3_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_3_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_3_0_win, 0,0,1,1)
        self.qtgui_freq_sink_x_3 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_3.set_update_time(0.10)
        self.qtgui_freq_sink_x_3.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_3.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3.enable_autoscale(False)
        self.qtgui_freq_sink_x_3.enable_grid(False)
        self.qtgui_freq_sink_x_3.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_3.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_3.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_3_win = sip.wrapinstance(self.qtgui_freq_sink_x_3.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_3_win, 1,0,1,1)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_2.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(False)
        self.qtgui_freq_sink_x_2.enable_grid(False)
        self.qtgui_freq_sink_x_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_2.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_2.set_plot_pos_half(not True)
        
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
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_2_win, 0,2,1,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
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
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_1_win, 0,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(disp_min, disp_max)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
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
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  7,
        	  (),
        	  1.0,
        	  100)
        self.pfb_channelizer_ccf_0.set_channel_map(([]))
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        	
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(91.5e6, 0)
        self.osmosdr_source_0.set_freq_corr(55, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(30, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.pfb_channelizer_ccf_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_3_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.qtgui_freq_sink_x_2, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.qtgui_freq_sink_x_3, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.qtgui_freq_sink_x_4, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.qtgui_freq_sink_x_5, 0))    
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.qtgui_freq_sink_x_6, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "bcfm_channelizer")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_6.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_5.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_4.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_3_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_3.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_disp_min(self):
        return self.disp_min

    def set_disp_min(self, disp_min):
        self.disp_min = disp_min
        self.qtgui_freq_sink_x_6.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_5.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_4.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_3_0.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_3.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_2.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_1.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.disp_min, self.disp_max)

    def get_disp_max(self):
        return self.disp_max

    def set_disp_max(self, disp_max):
        self.disp_max = disp_max
        self.qtgui_freq_sink_x_6.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_5.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_4.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_3_0.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_3.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_2.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_1.set_y_axis(self.disp_min, self.disp_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.disp_min, self.disp_max)


def main(top_block_cls=bcfm_channelizer, options=None):

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
