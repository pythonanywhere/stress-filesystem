if [ -z "$1" ]
    then
        TARG=/mnt/user_storage/bonnie/from-`hostname`
    else
        TARG=$1/bonnie/from-`hostname`
fi

for subdir in d1 d2 d3
do
    echo "creating dir for test at " $TARG/$subdir
    mkdir -p $TARG/$subdir
done

chmod -R 777 $TARG

bonnie++ -u nobody -p -1
bonnie++ -u nobody -p 3
for subdir in d1 d2 d3
do
    time bonnie++ -u nobody -ys -d $TARG/$subdir -n 4 -s 4096 > out_`date +%Ft%H%M`_`hostname`_$subdir.txt &
done
