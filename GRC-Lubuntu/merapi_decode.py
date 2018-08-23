#!/usr/bin/env python3


import sys,os
import curses
import math
import glob
import threading
import time
import datetime
import csv
import io

nframe=0
nsucc=0
nfail=0

filename=0
d_filename=0

filetime=0
d_filetime=0

var=['NO DATA','NO DATA','NO DATA','NO DATA','NO DATA','NO DATA']
sukses=0
 
def draw_menu(stdscr):
	while True:
		############################# SIGNAL PROCESSING AND DECODING ################################
		
		global filename
		global d_filename
		global var
		global sukses
		
		global nframe
		global nsucc
		global nfail

		global filetime
		global d_filetime

		try:
			list_of_files = glob.glob(os.environ.get("HOME")+'/*.dat') 
			waktu=os.path.getctime
			filename = max(list_of_files, key=waktu)
			
		except:
			filename=os.environ.get("HOME")+'/file_dummy.dat'
			file=open(filename,'w')

		if (filename != d_filename) and (d_filename != 0):
			os.remove(d_filename)

		d_filename=filename

		file = open(filename,'r')
		f_content=file.read()
		bitlen=len(f_content)

		##print(f_content)
		##print("found : %d bits"% (bitlen))

		global hor,ver,tem,gas,hum,air
	
		hor,ver,tem,gas,hum,air=0,0,0,0,0,0

		hor0,hor1,hor2,hor3=0,0,0,0
		ver0,ver1,ver2,ver3=0,0,0,0
		tem0,tem1,tem2,tem3=0,0,0,0
		gas0,gas1,gas2,gas3=0,0,0,0
		hum0,hum1,hum2,hum3=0,0,0,0
		air0,air1=0,0

		#detect bit transitions

		bit_trans_i=[]
		try:
			for a in range(0,bitlen-1):
				if f_content[a]!= f_content[a+1]:
					bit_trans_i.append(a)

		except:
			pass
		
		bit_trans_i_len=len(bit_trans_i)

		idx=0
		found='no'

		if bit_trans_i_len > 10:

			##############print(*bit_trans_i) #######################

			#calculate bit trans distance

			d_bit_trans_i=[1]
			d_bit_trans_i[0]=bit_trans_i[0]
			try:
				for b in range(0,bit_trans_i_len - 1):
					d_bit_trans_i.append(bit_trans_i[b+1]-bit_trans_i[b])
			except:
				pass

			#####################print(*d_bit_trans_i) #####################

			#reshape bits & decimate (maximum likelyhood clock recovery)

			d_bit_trans_len=len(d_bit_trans_i)
			try:
				for c in range(0,d_bit_trans_len):
					if d_bit_trans_i[c] < 5:
						d_bit_trans_i[c]=0
					else :
						if (d_bit_trans_i[c]%8) < 5:
							d_bit_trans_i[c]=math.floor(d_bit_trans_i[c]/8)
						else:
							d_bit_trans_i[c]=math.floor(d_bit_trans_i[c]/8)+1
			except:
				pass

			d_bit_trans_len=len(d_bit_trans_i)

			#################print(*d_bit_trans_i) #####################

			pattern=[3,1,2,1,2,1,1,2]

			try:
				for d in range(0,d_bit_trans_len-8):
					buff=[d_bit_trans_i[d],d_bit_trans_i[d+1],d_bit_trans_i[d+2],d_bit_trans_i[d+3],d_bit_trans_i[d+4],d_bit_trans_i[d+5],d_bit_trans_i[d+6],d_bit_trans_i[d+7]]
					if buff==pattern:
						idx=d
						##################3print("Found ! at %d"%(idx)) #####################
						found='yes'
						break
			except:
				pass

			bits=[]
			bit_count=0
			ntrans=0
			if found=='yes':
				e = idx
				try:
					for e in range(idx,d_bit_trans_len):
						if d_bit_trans_i[e] > 0:
							f=0
							if (ntrans%2)==0:
								for f in range(0,int(d_bit_trans_i[e])):
									bits.append(0)
									bit_count=bit_count+1
									if bit_count > 280:
										break
							else :
								for f in range(0,int(d_bit_trans_i[e])):
									bits.append(1)
									bit_count=bit_count+1
									if bit_count > 280:
										break
							ntrans=ntrans+1
							x=0

						if bit_count > 280:
							break
				except:
					bits=[0]*290
			
				############### print(*bits) #####################
				found='no'	

				byte_buff=0
				byte_data=[]
				for k in range(0,280,10):
					if bits[k+1] == 1:
						byte_buff=byte_buff+1
					if bits[k+2] == 1:
						byte_buff=byte_buff+2
					if bits[k+3] == 1:
						byte_buff=byte_buff+4
					if bits[k+4] == 1:
						byte_buff=byte_buff+8
					if bits[k+5] == 1:
						byte_buff=byte_buff+16
					if bits[k+6] == 1:
						byte_buff=byte_buff+32
					if bits[k+7] == 1:
						byte_buff=byte_buff+64
					if bits[k+8] == 1:
						byte_buff=byte_buff+128

					byte_data.append(byte_buff)
					byte_buff=0

				###########print(*byte_data) #####################

				# cek jika benar - benar printable
				sukses=1
				for l in range(0,28):
					if len(byte_data) > 1:
						if (byte_data[l] < 35) or (byte_data[l] > 90):
							sukses=0
					else :
						sukses=0
			
			
				if sukses==1:
					
					data_buff=[]
					for m in range(0,22):
						data_buff.append(byte_data[m+6])
						if (data_buff[m] < 58) and (data_buff[m] > 47):
							data_buff[m]=data_buff[m]-48

						elif (data_buff[m] < 71) and (data_buff[m] > 64):
							data_buff[m]=data_buff[m]-55

			
					i=0
					hor = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
					hor = hor / 20.0
					hor = round(hor*10)
					hor = hor / 10

					i=4
					ver = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
					ver = ver / 20.0
					ver = round(ver*10)
					ver = ver / 10

					i=8
					tem = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
					tem = tem / 10.0
					tem = round(tem*10)
					tem = tem / 10

					i=12
					gas = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
					gas = gas / 20.0
					gas = round(gas*10)
					gas = gas / 10

					i=16
					hum = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
					hum = 100*(34816 - hum)/28016
					hum = round(hum*10)
					hum = hum / 10

					i=20
					air = (data_buff[i]*16)+(data_buff[i+1])
					air = air * 1.5
					air = round(air*10)
					air = air / 10
					
					var = [str(hor),str(ver),str(tem),str(gas),str(hum),str(air)]

			else:
				#sukses=0
				pass
		else:
			#sukses=0
			pass

		stdscr=curses.initscr()

		# Clear and refresh the screen for a blank canvas
		stdscr.clear()
		curses.curs_set(0)
		
		k = 0
		x_min = 5
		x_max = 0
		y_min = 1
		y_max = 0

		y_max , x_max = stdscr.getmaxyx()

		y_table,x_table = y_min + 3, x_min + 2
		y_raw,x_raw = y_max-12,x_table

		sizeok=0

		curses.start_color()
		curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
		curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
		curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

		minimum_x=115
		minimum_y=30
		if (x_max >= minimum_x) and (y_max >= minimum_y):
			sizeok=1
		else:
			stdscr.box()
			stdscr.addstr(int(math.floor(y_max/2)) - 2,8,"Please Maximize The Window !",curses.A_BOLD)
			stdscr.addstr(int(math.floor(y_max/2)) - 1,8,"(min. %dchr X %dchr)"%(minimum_x,minimum_y),curses.A_BOLD)

		if sizeok == 1:
			stdscr.box()
			localtime = time.asctime( time.localtime(time.time()))
			time_text="\t Time now : " + localtime
			stdscr.addstr(y_min,x_min,"TELEMETRY DECODER - v0.1 \tMERAPI" + time_text,curses.A_BOLD)
			stdscr.addstr(y_max-2,x_min,"Handiko Gesang - Lab.SSTK UGM - 2018",curses.A_DIM)
			stdscr.addstr(y_max-2,x_table+59,"PRESS CTRL+C TO EXIT",curses.color_pair(1))
			stdscr.hline(y_min+1,1,'_',x_max-2)

			stdscr.addstr(y_table,x_table,"HORIZONTAL (v/v)",curses.A_BOLD)
			stdscr.addstr(y_table,x_table+19,"VERTICAL (v/v)",curses.A_BOLD)
			stdscr.addstr(y_table,x_table+36,"TEMPERATURE (deg.C)",curses.A_BOLD)
			stdscr.addstr(y_table,x_table+59,"GAS Cons. (ppm)",curses.A_BOLD)
			stdscr.addstr(y_table,x_table+78,"HUMIDITY (%)",curses.A_BOLD)
			stdscr.addstr(y_table,x_table+95,"RAIN (mm)",curses.A_BOLD)

			stdscr.hline(y_table+1,1,'_',x_max-2)

			
			if hor != 'NO DATA':
				if hor < 5:
					stdscr.addstr(y_table+3,x_table,var[0],curses.color_pair(2))
				else :
					stdscr.addstr(y_table+3,x_table,var[0],curses.color_pair(3))
			else:
				stdscr.addstr(y_table+3,x_table,var[0],curses.A_BOLD)


			if ver != 'NO DATA':
				if ver < 5:
					stdscr.addstr(y_table+3,x_table+19,var[1],curses.color_pair(2))
				else :
					stdscr.addstr(y_table+3,x_table+19,var[1],curses.color_pair(3))
			else:
				stdscr.addstr(y_table+3,x_table+20,var[1],curses.A_BOLD)


			if tem != 'NO DATA':
				if tem < 35:
					stdscr.addstr(y_table+3,x_table+36,var[2],curses.color_pair(2))
				else :
					stdscr.addstr(y_table+3,x_table+36,var[2],curses.color_pair(3))
			else:
				stdscr.addstr(y_table+3,x_table+38,var[2],curses.A_BOLD)


			if gas != 'NO DATA':
				if gas < 30:
					stdscr.addstr(y_table+3,x_table+59,var[3],curses.color_pair(2))
				else :
					stdscr.addstr(y_table+3,x_table+59,var[3],curses.color_pair(3))
			else:
				stdscr.addstr(y_table+3,x_table+62,var[3],curses.A_BOLD)

			
			if hum != 'NO DATA':
				stdscr.addstr(y_table+3,x_table+78,var[4],curses.color_pair(2))
			else:
				stdscr.addstr(y_table+3,x_table+78,var[4],curses.A_BOLD)
			

			if air != 'NO DATA':
				if air < 15:
					stdscr.addstr(y_table+3,x_table+95,var[5],curses.color_pair(2))
				else :
					stdscr.addstr(y_table+3,x_table+95,var[5],curses.color_pair(3))
			else:
				stdscr.addstr(y_table+3,x_table+98,var[5],curses.A_BOLD)
			

			t=datetime.datetime.fromtimestamp(os.path.getctime('/home/handiko'))
			frame_time="Last received : " + time.ctime(os.path.getctime(filename))
			if sukses==1:
				stdscr.addstr(y_table+10,x_table,frame_time)
			else:
				stdscr.addstr(y_table+10,x_table,"NO DATA RECEIVED YET")

			stdscr.hline(y_raw-2,1,'_',x_max-2)
			stdscr.addstr(y_raw,x_table,"Latest Raw Data",curses.A_BOLD)
			stdscr.addstr(y_raw,x_table+59,"Debug",curses.A_BOLD)
			stdscr.hline(y_raw+1,1,'_',x_max-2)
			if sukses==1:
				stdscr.addstr(y_raw+3,x_table,"%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c#"% (\
				byte_data[0],byte_data[1],byte_data[2],byte_data[3],byte_data[4],byte_data[5],byte_data[6],\
				byte_data[7],byte_data[8],byte_data[9],byte_data[10],byte_data[11],byte_data[12],byte_data[13],\
				byte_data[14],byte_data[15],byte_data[16],byte_data[17],byte_data[18],byte_data[19],byte_data[20],\
				byte_data[21],byte_data[22],byte_data[23],byte_data[24],byte_data[25],byte_data[26],byte_data[27]))

				i=0
				hor = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
				stdscr.addstr(y_raw+3,x_table+59,"HOR        %04X   %d"%(hor,hor))
				
				i=4
				ver = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
				stdscr.addstr(y_raw+4,x_table+59,"VER        %04X   %d"%(ver,ver))

				i=8
				tem = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
				stdscr.addstr(y_raw+5,x_table+59,"TEMP       %04X   %d"%(tem,tem))

				i=12
				gas = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
				stdscr.addstr(y_raw+6,x_table+59,"GAS        %04X   %d"%(gas,gas))

				i=16
				hum = (data_buff[i]*4096)+(data_buff[i+1]*256)+(data_buff[i+2]*16)+(data_buff[i+3])
				stdscr.addstr(y_raw+7,x_table+59,"HUMIDITY   %04X   %d"%(hum,hum))

				i=20
				air = (data_buff[i]*16)+(data_buff[i+1])
				stdscr.addstr(y_raw+8,x_table+59,"RAIN       %04X   %d"%(air,air))

				filetime=time.ctime(os.path.getctime(filename))
				csv_text = [[filetime,"HOR = ",var[0],"VER = ",var[1],"TEM = ",var[2],"GAS = ",var[3],"HUM = ",var[4],"RAI = ",var[5]]]
				if (filetime != d_filetime) and (d_filetime != 0):
					csvfile=open(os.environ.get("HOME")+'/log.csv','a')
					with csvfile:
						writer = csv.writer(csvfile)
						for row in csv_text:
							writer.writerow(row)

				d_filetime=filetime
				
			else:
				stdscr.addstr(y_raw+3,x_table,"NO DATA")

			stdscr.refresh()

    			
		time.sleep(0.75)


def main():
	curses.wrapper(draw_menu)

if __name__ == "__main__":
	main()




