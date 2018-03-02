#!/usr/bin/python

import os
import subprocess


#benchmarks = ['BFS12','convtex12', 'dct12', 'fwt12', 'LIB12', 'monte12', 'MUM12', 'NN12', 'NQU12', 'RAY12', 'STO12' ]
benchmarks = ['STO12']
works = ['bin','bin_new_journal','bin_XYYX', 'bin_new', 'bin_DA2', 'bin_cfnoc']
d = dict(os.environ)
d["SC_SIGNAL_WRITE_CHECK"] = 'DISABLE'
NUM_CORES = 132

for bench in benchmarks:
	for i in range(NUM_CORES):
		copy_path = '/media/yaswanth/nasstore/gpu_traces/%s/node[%d].txt' % (bench, i)
		subprocess.call(['cp', copy_path, '.'])
	for w in works:
		os.chdir(w)
		#copy the traces to the binary directory of noxim works
		for i in range(NUM_CORES):
			copy_path = '../node[%d].txt' % (i)
			subprocess.call(['cp', copy_path, '.'])
		#execute the noxim command
		noxim_cmd = './noxim -pir 0.01 poisson -sim 100000 -warmup 100 -size 8 8 -buffer 12 -pwr default_router.pwr -lpls -qos 0.5 -routing xy -dimx 12 -dimy 12 -traffic benchmark'
		cmd = noxim_cmd.split()
		with open('test.log', 'w') as outfile:
			subprocess.call(noxim_cmd, shell=True, env = d, stdout = outfile)
		# get the tail of the output file and save it in the results.log
		with open(bench+'.log', 'w')as of:
			subprocess.call(['tail', '-100', 'test.log'], stdout = of)
		os.chdir('..')
	
	
