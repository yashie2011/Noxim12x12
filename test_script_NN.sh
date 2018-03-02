#!/bin/sh

cmd="./noxim -pir 0.01 poisson -sim 100000 -warmup 100 -size 8 8 -buffer 12 -pwr default_router.pwr -lpls -qos 0.5 -routing xy -dimx 12 -dimy 12 -traffic benchmark"

cd bin
echo "current dir $PWD"
find /media/yaswanth/nasstore/gpu_traces/NN12 -name "node\[*" -exec "cp" "{}" . ";"
echo "copied traces to $PWD"
$cmd > NN12.log


cd ../bin_XYYX
echo "current dir $PWD"
find ../bin -name "node\[*" -exec "cp" "{}" . ";"
echo "copied traces to $PWD" 
rm ../bin/node\[*
$cmd > NN12.log


cd ../bin_new
echo "current dir $PWD"
find ../bin_XYYX -name "node\[*" -exec "cp" "{}" . ";"
echo "copied traces to $PWD"
rm ../bin_XYYX/node\[*
##$cmd > NN12.log

cd ../bin_new_journal
echo "current dir $PWD"
find ../bin_new -name "node\[*" -exec "cp" "{}" . ";"
echo "copied traces to $PWD"
rm ../bin_new/node\[*
$cmd > NN12.log

cd ../bin_DA2
echo "current dir $PWD"
find ../bin_new_journal -name "node\[*" -exec "cp" "{}" . ";"
echo "copied traces to $PWD"
rm ../bin_new_journal/node\[*
$cmd > NN12.log

cd ../bin_cfnoc
echo "current dir $PWD"
find ../bin_DA2 -name "node\[*" -exec "cp" "{}" . ";"
echo "copied traces to $PWD"
rm ../bin_DA2/node\[*
$cmd > NN12.log
rm node\[*

echo "Done."

cd ..
exit 0
