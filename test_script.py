#!/usr/bin/python

import os
import subprocess


benchmarks = ['BFS8','convtex8','dct8x8', 'fwt8', 'LIB8', 'monte8', 'MUM8', 'NN8', 'NQU8', 'RAY8', 'STO8' ]
#benchmarks = ['BFS8', 'dct8x8', 'LIB8','monte8']
#works = ['bin','bin_new_journal','bin_XYYX', 'bin_new', 'bin_DA2', 'bin_cfnoc']

for bench in benchmarks:
	subprocess.call(['./test_script_faster.sh', bench])
	
