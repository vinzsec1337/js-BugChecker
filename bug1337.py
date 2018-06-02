try:
	from platform import python_version as v
	from socket import setdefaulttimeout
	from datetime import datetime as dt
	from socket import gethostbyname
	from socket import SOCK_STREAM
	from platform import system as OS
	from socket import AF_INET
	from socket import socket
	from re import findall as f
	from socket import error
	from time import sleep
	from sys import argv
	from sys import exit
except ImportError as e:
	print('[!] Module %s tidak ada bos....'%str(e).split(' ')[-1])
	exit(1)
d = {
	'hos':'',
	'met':'',
	'pro':'',
	'pay':'',
	'tim':'',
	}
hpp = 0
ppp = 0
mpp = 0
jml = ''
info = '''\rk###                                                           ###
#   \rh mmmmm  mmmmm  mmmmm  m    m   mm   mm   m  mmmm  m    m   \rk #
#   \rh #   "#   #    #   "# ##  ##   ##   #"m  # #"   "  #  #    \rk #
#   \rh #mmm#"   #    #mmmm" # ## #  #  #  # #m # "#mmm    ##     \rk #
#   \rh #        #    #   "m # "" #  #mm#  #  # #     "#  m""m    \rk #
#   \rh #      mm#mm  #    " #    # #    # #   ## "mmm#" m"  "m   \rk #
#                                                               #
#    \rm*\rkName : \rhBugChecker.py, python2, versi 0.1                    \rk #
#    \rm*\rkBy   : \rhElang X-CoderID \rb/// \rmAndroSec1337                       \rk #
#    \rm*\rkDate : \rhSabtu 02 Juni 2018                                 \rk #
###                                                           ###'''
setting = '''
# Name : BugChecker.py python2 versi 0.1
# By   : Elang X-CoderID aka AndroSec1337
# Date : Sabtu 02 Juni 2018
*file setting BugChecker.py*
*ket*
** 'hos' adalah calon bug tambah ';' jika cek host ganda...ato lebih
       contoh : hos=host000.com;host001.net
** 'met' adalah method tambah ';' jika cek method ganda....ato lebih
       contoh : met=GET;DELETE
** 'pro' adalah proxy:port tambah ';' jika cek proxy ganda....
       contoh : pro=111.222.333.444:1234;000.999.888.777:8080
** 'pay' adalah payload ... dimana ...
      [m] adalah method
      [h] adalah host
      [cr] adalah '\\r'
      [lf] adalah '\\n'
      [crlf] adalah '\\r\\n'
      *jika belum mahir ane saranin jangan di ubah...
** 'tim' adalah waktu habis(time out) dalam satuan detik.
      contoh: tim=3
####################################
hos=line.me
met=PUT;GET;POST;HEAD;PATCH;TRACE;DELETE;OPTIONS;CONNECT
pro=10.8.3.8:8080
pay=[m] http://[h]/ HTTP/1.1[crlf]Host: [h][crlf][crlf]
tim=5
####################################
'''
def main():
	global d,hpp,ppp,mpp,jml
	hos = []
	pro = []
	met = []
	tamp('\rk'+'#'*65)
	tamp(info)
	tamp('\rk'+'#'*65)
	jeda(3)
	tamp('\rh[+] memuat dan mengecek file setting...')
	jeda(1.5)
	getset()
	cekpay()
	jeda(1.5)
	tamp('\rh[+] payload oke...')
	jeda(1.5)
	tamp('\rh[+] file setting...')
	jeda(1.5)
	tamp('\rh[+]\rk payload__\rm#\rc'+d['pay'])
	tamp('\rh[+]\rk methode__\rm#\rc'+d['met'])
	tamp('\rh[+]\rk proxy____\rm#\rc'+d['pro'])
	tamp('\rh[+]\rk time out_\rm#\rc'+d['tim'])
	tamp('\rh[+] cek semua host...')
	jeda(1.5)
	setdefaulttimeout(int(d['tim']))
	d['pay'] = d['pay'].replace('[cr]','\r')
	d['pay'] = d['pay'].replace('[lf]','\n')
	d['pay'] = d['pay'].replace('[crlf]','\r\n')
	c = ''
	for h in d['hos'].split(';'):
		if len(h) != 0:
			if cek(h) == 1:
				if len(h) > hpp:hpp = len(h)
				hos.append(h)
	tamp('\rh[+] cek selesai...')
	jeda(1.5)
	if len(hos) == 0:
		tamp('\rm[!] tidak ada host yang aktif...')
		tamp('\rk'+'#'*65)
		exit(1)
	tamp('\rh[+] list host aktif...')
	jeda(1.5)
	for h in hos:
			jeda(0.05)
			tamp('\rb==> \rk'+h)
	tamp('\rh[+] cek semua respon host...')
	jeda(1.5)
	waktu0 = dt.now()
	for p in d['pro'].split(';'):
			p = p.replace(' ','')
			if len(p) != 0:
				if len(p) > ppp:ppp = len(p)
				pro.append(p)
	for m in d['met'].split(';'):
			m = m.replace(' ','')
			if len(m) != 0:
				if len(m) > mpp:mpp = len(m)
				met.append(m)
	jml = str(len(pro)*len(met)*len(hos))
	i = 1
	for h in hos:
		for m in met:
			for p in pro:
				pay = d['pay'].replace('[h]',h)
				pay = pay.replace('[m]',m)
				get(pay,p,h,m
