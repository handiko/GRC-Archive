#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Belajar Dsp
# Generated: Mon Apr 16 21:03:44 2018
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
import numpy
import sip
import sys


class belajar_dsp(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Belajar Dsp")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Belajar Dsp")
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

        self.settings = Qt.QSettings("GNU Radio", "belajar_dsp")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.samp_rate = samp_rate = 32000
        self.nfilt = nfilt = 32
        self.tx_samp_rate = tx_samp_rate = samp_rate * sps
        self.rrc_symb_rate = rrc_symb_rate = 1.0
        self.rrc_samp_rate = rrc_samp_rate = nfilt*sps
        self.rrc_n_taps = rrc_n_taps = 3*nfilt*sps
        self.rrc_gain = rrc_gain = nfilt
        self.ex_bw = ex_bw = 0.35
        self.updt_period = updt_period = 0.02
        self.symb_rate = symb_rate = tx_samp_rate / sps
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(rrc_gain, rrc_samp_rate, rrc_symb_rate, ex_bw, rrc_n_taps)
        self.costas_loop_bw = costas_loop_bw = -30
        self.cma_gain = cma_gain = -30
        self.clock_sync_loop_bw = clock_sync_loop_bw = -20
        self.clock_ppm = clock_ppm = 50

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Symbols')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Interpolated')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'RRC Filtered')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'Clock Synched')
        self.tab_widget_4 = Qt.QWidget()
        self.tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_4)
        self.tab_grid_layout_4 = Qt.QGridLayout()
        self.tab_layout_4.addLayout(self.tab_grid_layout_4)
        self.tab.addTab(self.tab_widget_4, 'CMA Output')
        self.tab_widget_5 = Qt.QWidget()
        self.tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_5)
        self.tab_grid_layout_5 = Qt.QGridLayout()
        self.tab_layout_5.addLayout(self.tab_grid_layout_5)
        self.tab.addTab(self.tab_widget_5, 'Channel')
        self.tab_widget_6 = Qt.QWidget()
        self.tab_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_6)
        self.tab_grid_layout_6 = Qt.QGridLayout()
        self.tab_layout_6.addLayout(self.tab_grid_layout_6)
        self.tab.addTab(self.tab_widget_6, 'Clock Synched - Channel')
        self.tab_widget_7 = Qt.QWidget()
        self.tab_layout_7 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_7)
        self.tab_grid_layout_7 = Qt.QGridLayout()
        self.tab_layout_7.addLayout(self.tab_grid_layout_7)
        self.tab.addTab(self.tab_widget_7, 'CMA Output - Channel')
        self.tab_widget_8 = Qt.QWidget()
        self.tab_layout_8 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_8)
        self.tab_grid_layout_8 = Qt.QGridLayout()
        self.tab_layout_8.addLayout(self.tab_grid_layout_8)
        self.tab.addTab(self.tab_widget_8, 'Costas Loop - Channel')
        self.top_layout.addWidget(self.tab)
        self._costas_loop_bw_range = Range(-30, -3, 1, -30, 200)
        self._costas_loop_bw_win = RangeWidget(self._costas_loop_bw_range, self.set_costas_loop_bw, "costas_loop_bw", "counter_slider", float)
        self.top_grid_layout.addWidget(self._costas_loop_bw_win, 1,2,1,1)
        self._cma_gain_range = Range(-30, -3, 1, -30, 200)
        self._cma_gain_win = RangeWidget(self._cma_gain_range, self.set_cma_gain, "cma_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._cma_gain_win, 1,1,1,1)
        self._clock_sync_loop_bw_range = Range(-30, -3, 1, -20, 200)
        self._clock_sync_loop_bw_win = RangeWidget(self._clock_sync_loop_bw_range, self.set_clock_sync_loop_bw, "clock_sync_loop_bw", "counter_slider", float)
        self.top_grid_layout.addWidget(self._clock_sync_loop_bw_win, 1,0,1,1)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, tx_samp_rate, symb_rate, 0.35, 11*tx_samp_rate/symb_rate))
        self.qtgui_time_sink_x_8 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_8.set_update_time(updt_period)
        self.qtgui_time_sink_x_8.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_8.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_8.enable_tags(-1, True)
        self.qtgui_time_sink_x_8.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_8.enable_autoscale(True)
        self.qtgui_time_sink_x_8.enable_grid(False)
        self.qtgui_time_sink_x_8.enable_axis_labels(True)
        self.qtgui_time_sink_x_8.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_8.disable_legend()
        
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_8.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_8.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_8.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_8.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_8.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_8.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_8.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_8.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_8_win = sip.wrapinstance(self.qtgui_time_sink_x_8.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_8.addWidget(self._qtgui_time_sink_x_8_win, 0,0,1,2)
        self.qtgui_time_sink_x_7 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_7.set_update_time(updt_period)
        self.qtgui_time_sink_x_7.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_7.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_7.enable_tags(-1, True)
        self.qtgui_time_sink_x_7.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_7.enable_autoscale(True)
        self.qtgui_time_sink_x_7.enable_grid(False)
        self.qtgui_time_sink_x_7.enable_axis_labels(True)
        self.qtgui_time_sink_x_7.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_7.disable_legend()
        
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_7.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_7.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_7.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_7.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_7.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_7.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_7.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_7.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_7_win = sip.wrapinstance(self.qtgui_time_sink_x_7.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_7.addWidget(self._qtgui_time_sink_x_7_win, 0,0,1,2)
        self.qtgui_time_sink_x_6 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate*2, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_6.set_update_time(updt_period)
        self.qtgui_time_sink_x_6.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_6.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_6.enable_tags(-1, True)
        self.qtgui_time_sink_x_6.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_6.enable_autoscale(True)
        self.qtgui_time_sink_x_6.enable_grid(False)
        self.qtgui_time_sink_x_6.enable_axis_labels(True)
        self.qtgui_time_sink_x_6.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_6.disable_legend()
        
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_6.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_6.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_6.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_6.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_6.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_6.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_6.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_6.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_6_win = sip.wrapinstance(self.qtgui_time_sink_x_6.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_6.addWidget(self._qtgui_time_sink_x_6_win, 0,0,1,2)
        self.qtgui_time_sink_x_5 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_5.set_update_time(updt_period)
        self.qtgui_time_sink_x_5.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_5.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_5.enable_tags(-1, True)
        self.qtgui_time_sink_x_5.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_5.enable_autoscale(True)
        self.qtgui_time_sink_x_5.enable_grid(False)
        self.qtgui_time_sink_x_5.enable_axis_labels(True)
        self.qtgui_time_sink_x_5.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_5.disable_legend()
        
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_5.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_5.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_5.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_5.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_5.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_5.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_5.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_5.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_5_win = sip.wrapinstance(self.qtgui_time_sink_x_5.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_5.addWidget(self._qtgui_time_sink_x_5_win, 0,0,1,2)
        self.qtgui_time_sink_x_4 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_4.set_update_time(updt_period)
        self.qtgui_time_sink_x_4.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_4.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_4.enable_tags(-1, True)
        self.qtgui_time_sink_x_4.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_4.enable_autoscale(True)
        self.qtgui_time_sink_x_4.enable_grid(False)
        self.qtgui_time_sink_x_4.enable_axis_labels(True)
        self.qtgui_time_sink_x_4.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_4.disable_legend()
        
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_4.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_4.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_4.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_4.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_4.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_4.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_4.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_4.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_4_win = sip.wrapinstance(self.qtgui_time_sink_x_4.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_4_win, 0,0,1,2)
        self.qtgui_time_sink_x_3 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate*2, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_3.set_update_time(updt_period)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_3.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_3.enable_tags(-1, True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3.enable_autoscale(True)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_axis_labels(True)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_3.disable_legend()
        
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_3.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_3.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_3_win, 0,0,1,2)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate*sps, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(updt_period)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(True)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        
        if not True:
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_2_win, 0,0,1,2)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate*sps, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(updt_period)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_1_win, 0,0,1,2)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(updt_period)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 0,0,1,2)
        self.qtgui_freq_sink_x_8 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_8.set_update_time(updt_period)
        self.qtgui_freq_sink_x_8.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_8.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_8.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_8.enable_autoscale(False)
        self.qtgui_freq_sink_x_8.enable_grid(False)
        self.qtgui_freq_sink_x_8.set_fft_average(1.0)
        self.qtgui_freq_sink_x_8.enable_axis_labels(True)
        self.qtgui_freq_sink_x_8.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_8.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_8.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_8.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_8.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_8.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_8.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_8.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_8_win = sip.wrapinstance(self.qtgui_freq_sink_x_8.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_8.addWidget(self._qtgui_freq_sink_x_8_win, 1,0,1,1)
        self.qtgui_freq_sink_x_7 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_7.set_update_time(updt_period)
        self.qtgui_freq_sink_x_7.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_7.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_7.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_7.enable_autoscale(False)
        self.qtgui_freq_sink_x_7.enable_grid(False)
        self.qtgui_freq_sink_x_7.set_fft_average(1.0)
        self.qtgui_freq_sink_x_7.enable_axis_labels(True)
        self.qtgui_freq_sink_x_7.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_7.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_7.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_7.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_7.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_7.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_7.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_7.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_7_win = sip.wrapinstance(self.qtgui_freq_sink_x_7.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_7.addWidget(self._qtgui_freq_sink_x_7_win, 1,0,1,1)
        self.qtgui_freq_sink_x_6 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*2, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_6.set_update_time(updt_period)
        self.qtgui_freq_sink_x_6.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_6.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_6.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_6.enable_autoscale(False)
        self.qtgui_freq_sink_x_6.enable_grid(False)
        self.qtgui_freq_sink_x_6.set_fft_average(1.0)
        self.qtgui_freq_sink_x_6.enable_axis_labels(True)
        self.qtgui_freq_sink_x_6.enable_control_panel(False)
        
        if not True:
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
        self.tab_grid_layout_6.addWidget(self._qtgui_freq_sink_x_6_win, 1,0,1,1)
        self.qtgui_freq_sink_x_5 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_5.set_update_time(updt_period)
        self.qtgui_freq_sink_x_5.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_5.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_5.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_5.enable_autoscale(False)
        self.qtgui_freq_sink_x_5.enable_grid(False)
        self.qtgui_freq_sink_x_5.set_fft_average(1.0)
        self.qtgui_freq_sink_x_5.enable_axis_labels(True)
        self.qtgui_freq_sink_x_5.enable_control_panel(False)
        
        if not True:
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
        self.tab_grid_layout_5.addWidget(self._qtgui_freq_sink_x_5_win, 1,0,1,1)
        self.qtgui_freq_sink_x_4 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_4.set_update_time(updt_period)
        self.qtgui_freq_sink_x_4.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_4.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_4.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_4.enable_autoscale(False)
        self.qtgui_freq_sink_x_4.enable_grid(False)
        self.qtgui_freq_sink_x_4.set_fft_average(1.0)
        self.qtgui_freq_sink_x_4.enable_axis_labels(True)
        self.qtgui_freq_sink_x_4.enable_control_panel(False)
        
        if not True:
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
        self.tab_grid_layout_4.addWidget(self._qtgui_freq_sink_x_4_win, 1,0,1,1)
        self.qtgui_freq_sink_x_3 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*2, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_3.set_update_time(updt_period)
        self.qtgui_freq_sink_x_3.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_3.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3.enable_autoscale(False)
        self.qtgui_freq_sink_x_3.enable_grid(False)
        self.qtgui_freq_sink_x_3.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3.enable_control_panel(False)
        
        if not True:
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
        self.tab_grid_layout_3.addWidget(self._qtgui_freq_sink_x_3_win, 1,0,1,1)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*sps, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_2.set_update_time(updt_period)
        self.qtgui_freq_sink_x_2.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(False)
        self.qtgui_freq_sink_x_2.enable_grid(False)
        self.qtgui_freq_sink_x_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)
        
        if not True:
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
        self.tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_2_win, 1,0,1,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*sps, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(updt_period)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
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
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_1_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(updt_period)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
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
        self.tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 1,0,1,1)
        self.qtgui_const_sink_x_8 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_8.set_update_time(updt_period)
        self.qtgui_const_sink_x_8.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_8.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_8.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_8.enable_autoscale(True)
        self.qtgui_const_sink_x_8.enable_grid(False)
        self.qtgui_const_sink_x_8.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_8.disable_legend()
        
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
                self.qtgui_const_sink_x_8.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_8.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_8.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_8.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_8.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_8.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_8.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_8_win = sip.wrapinstance(self.qtgui_const_sink_x_8.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_8.addWidget(self._qtgui_const_sink_x_8_win, 1,1,1,1)
        self.qtgui_const_sink_x_7 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_7.set_update_time(updt_period)
        self.qtgui_const_sink_x_7.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_7.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_7.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_7.enable_autoscale(True)
        self.qtgui_const_sink_x_7.enable_grid(False)
        self.qtgui_const_sink_x_7.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_7.disable_legend()
        
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
                self.qtgui_const_sink_x_7.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_7.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_7.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_7.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_7.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_7.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_7.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_7_win = sip.wrapinstance(self.qtgui_const_sink_x_7.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_7.addWidget(self._qtgui_const_sink_x_7_win, 1,1,1,1)
        self.qtgui_const_sink_x_6 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_6.set_update_time(updt_period)
        self.qtgui_const_sink_x_6.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_6.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_6.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_6.enable_autoscale(True)
        self.qtgui_const_sink_x_6.enable_grid(False)
        self.qtgui_const_sink_x_6.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_6.disable_legend()
        
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
                self.qtgui_const_sink_x_6.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_6.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_6.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_6.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_6.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_6.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_6.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_6_win = sip.wrapinstance(self.qtgui_const_sink_x_6.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_6.addWidget(self._qtgui_const_sink_x_6_win, 1,1,1,1)
        self.qtgui_const_sink_x_5 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_5.set_update_time(updt_period)
        self.qtgui_const_sink_x_5.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_5.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_5.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_5.enable_autoscale(True)
        self.qtgui_const_sink_x_5.enable_grid(False)
        self.qtgui_const_sink_x_5.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_5.disable_legend()
        
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
                self.qtgui_const_sink_x_5.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_5.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_5.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_5.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_5.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_5.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_5.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_5_win = sip.wrapinstance(self.qtgui_const_sink_x_5.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_5.addWidget(self._qtgui_const_sink_x_5_win, 1,1,1,1)
        self.qtgui_const_sink_x_4 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_4.set_update_time(updt_period)
        self.qtgui_const_sink_x_4.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_4.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_4.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_4.enable_autoscale(True)
        self.qtgui_const_sink_x_4.enable_grid(False)
        self.qtgui_const_sink_x_4.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_4.disable_legend()
        
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
                self.qtgui_const_sink_x_4.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_4.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_4.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_4.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_4.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_4.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_4.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_4_win = sip.wrapinstance(self.qtgui_const_sink_x_4.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_4.addWidget(self._qtgui_const_sink_x_4_win, 1,1,1,1)
        self.qtgui_const_sink_x_3 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_3.set_update_time(updt_period)
        self.qtgui_const_sink_x_3.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_3.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_3.enable_autoscale(True)
        self.qtgui_const_sink_x_3.enable_grid(False)
        self.qtgui_const_sink_x_3.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_3.disable_legend()
        
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
                self.qtgui_const_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_3.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_3_win = sip.wrapinstance(self.qtgui_const_sink_x_3.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_const_sink_x_3_win, 1,1,1,1)
        self.qtgui_const_sink_x_2 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_2.set_update_time(updt_period)
        self.qtgui_const_sink_x_2.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_2.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_2.enable_autoscale(True)
        self.qtgui_const_sink_x_2.enable_grid(False)
        self.qtgui_const_sink_x_2.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_2.disable_legend()
        
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
                self.qtgui_const_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_2_win = sip.wrapinstance(self.qtgui_const_sink_x_2.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_const_sink_x_2_win, 1,1,1,1)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(updt_period)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1.disable_legend()
        
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
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_const_sink_x_1_win, 1,1,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(updt_period)
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
        self.tab_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_win, 1,1,1,1)
        self.digital_pfb_clock_sync_xxx_1 = digital.pfb_clock_sync_ccf(sps, 6.28 / 200 + 0*pow(10,clock_sync_loop_bw/10), (rrc_taps), nfilt, nfilt/2, 0.5, 1)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 6.28 / 200, (rrc_taps), nfilt, nfilt/2, 1.5, 1)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(6.28 / 50 + 0*pow(10,costas_loop_bw/10), 4, False)
        self.digital_cma_equalizer_cc_1 = digital.cma_equalizer_cc(32, 1, pow(10,cma_gain/10), 1)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(32, 1, pow(10,cma_gain/10), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((0.5+0.5j, 0.5-0.5j, -0.5-0.5j, -0.5+0.5j), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.1,
        	frequency_offset=0.0,
        	epsilon=1.0 + clock_ppm*1e-6,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate/sps,True)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, sps)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 4, 100000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.qtgui_const_sink_x_1, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.digital_pfb_clock_sync_xxx_1, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_const_sink_x_5, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_5, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_time_sink_x_5, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_const_sink_x_4, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_freq_sink_x_4, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_time_sink_x_4, 0))    
        self.connect((self.digital_cma_equalizer_cc_1, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_1, 0), (self.qtgui_const_sink_x_7, 0))    
        self.connect((self.digital_cma_equalizer_cc_1, 0), (self.qtgui_freq_sink_x_7, 0))    
        self.connect((self.digital_cma_equalizer_cc_1, 0), (self.qtgui_time_sink_x_7, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_8, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_freq_sink_x_8, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_time_sink_x_8, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_3, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_freq_sink_x_3, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_time_sink_x_3, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_1, 0), (self.digital_cma_equalizer_cc_1, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_1, 0), (self.qtgui_const_sink_x_6, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_1, 0), (self.qtgui_freq_sink_x_6, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_1, 0), (self.qtgui_time_sink_x_6, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_const_sink_x_2, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_freq_sink_x_2, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_time_sink_x_2, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "belajar_dsp")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_tx_samp_rate(self.samp_rate * self.sps)
        self.set_symb_rate(self.tx_samp_rate / self.sps)
        self.set_rrc_samp_rate(self.nfilt*self.sps)
        self.set_rrc_n_taps(3*self.nfilt*self.sps)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate*self.sps)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate*self.sps)
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate*self.sps)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.sps)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/self.sps)
        self.blocks_repeat_0.set_interpolation(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_tx_samp_rate(self.samp_rate * self.sps)
        self.qtgui_time_sink_x_8.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_7.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_6.set_samp_rate(self.samp_rate*2)
        self.qtgui_time_sink_x_5.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_4.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_3.set_samp_rate(self.samp_rate*2)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate*self.sps)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate*self.sps)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_8.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_7.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_6.set_frequency_range(0, self.samp_rate*2)
        self.qtgui_freq_sink_x_5.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_4.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_3.set_frequency_range(0, self.samp_rate*2)
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate*self.sps)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.sps)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/self.sps)

    def get_nfilt(self):
        return self.nfilt

    def set_nfilt(self, nfilt):
        self.nfilt = nfilt
        self.set_rrc_samp_rate(self.nfilt*self.sps)
        self.set_rrc_n_taps(3*self.nfilt*self.sps)
        self.set_rrc_gain(self.nfilt)

    def get_tx_samp_rate(self):
        return self.tx_samp_rate

    def set_tx_samp_rate(self, tx_samp_rate):
        self.tx_samp_rate = tx_samp_rate
        self.set_symb_rate(self.tx_samp_rate / self.sps)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.tx_samp_rate, self.symb_rate, 0.35, 11*self.tx_samp_rate/self.symb_rate))

    def get_rrc_symb_rate(self):
        return self.rrc_symb_rate

    def set_rrc_symb_rate(self, rrc_symb_rate):
        self.rrc_symb_rate = rrc_symb_rate
        self.set_rrc_taps(firdes.root_raised_cosine(self.rrc_gain, self.rrc_samp_rate, self.rrc_symb_rate, self.ex_bw, self.rrc_n_taps))

    def get_rrc_samp_rate(self):
        return self.rrc_samp_rate

    def set_rrc_samp_rate(self, rrc_samp_rate):
        self.rrc_samp_rate = rrc_samp_rate
        self.set_rrc_taps(firdes.root_raised_cosine(self.rrc_gain, self.rrc_samp_rate, self.rrc_symb_rate, self.ex_bw, self.rrc_n_taps))

    def get_rrc_n_taps(self):
        return self.rrc_n_taps

    def set_rrc_n_taps(self, rrc_n_taps):
        self.rrc_n_taps = rrc_n_taps
        self.set_rrc_taps(firdes.root_raised_cosine(self.rrc_gain, self.rrc_samp_rate, self.rrc_symb_rate, self.ex_bw, self.rrc_n_taps))

    def get_rrc_gain(self):
        return self.rrc_gain

    def set_rrc_gain(self, rrc_gain):
        self.rrc_gain = rrc_gain
        self.set_rrc_taps(firdes.root_raised_cosine(self.rrc_gain, self.rrc_samp_rate, self.rrc_symb_rate, self.ex_bw, self.rrc_n_taps))

    def get_ex_bw(self):
        return self.ex_bw

    def set_ex_bw(self, ex_bw):
        self.ex_bw = ex_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.rrc_gain, self.rrc_samp_rate, self.rrc_symb_rate, self.ex_bw, self.rrc_n_taps))

    def get_updt_period(self):
        return self.updt_period

    def set_updt_period(self, updt_period):
        self.updt_period = updt_period
        self.qtgui_time_sink_x_8.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_7.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_6.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_5.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_4.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_3.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_2.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_1.set_update_time(self.updt_period)
        self.qtgui_time_sink_x_0.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_8.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_7.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_6.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_5.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_4.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_3.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_2.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_1.set_update_time(self.updt_period)
        self.qtgui_freq_sink_x_0.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_8.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_7.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_6.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_5.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_4.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_3.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_2.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_1.set_update_time(self.updt_period)
        self.qtgui_const_sink_x_0.set_update_time(self.updt_period)

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.tx_samp_rate, self.symb_rate, 0.35, 11*self.tx_samp_rate/self.symb_rate))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_1.update_taps((self.rrc_taps))
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_costas_loop_bw(self):
        return self.costas_loop_bw

    def set_costas_loop_bw(self, costas_loop_bw):
        self.costas_loop_bw = costas_loop_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(6.28 / 50 + 0*pow(10,self.costas_loop_bw/10))

    def get_cma_gain(self):
        return self.cma_gain

    def set_cma_gain(self, cma_gain):
        self.cma_gain = cma_gain
        self.digital_cma_equalizer_cc_1.set_gain(pow(10,self.cma_gain/10))
        self.digital_cma_equalizer_cc_0.set_gain(pow(10,self.cma_gain/10))

    def get_clock_sync_loop_bw(self):
        return self.clock_sync_loop_bw

    def set_clock_sync_loop_bw(self, clock_sync_loop_bw):
        self.clock_sync_loop_bw = clock_sync_loop_bw
        self.digital_pfb_clock_sync_xxx_1.set_loop_bandwidth(6.28 / 200 + 0*pow(10,self.clock_sync_loop_bw/10))

    def get_clock_ppm(self):
        return self.clock_ppm

    def set_clock_ppm(self, clock_ppm):
        self.clock_ppm = clock_ppm
        self.channels_channel_model_0.set_timing_offset(1.0 + self.clock_ppm*1e-6)


def main(top_block_cls=belajar_dsp, options=None):

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
